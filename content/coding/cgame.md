Title: cgame: C entity-component-system, 2d sprites, Lua scripting, save/load
Slug: cgame
Date: 2014-1-1
Summary: a week of C coding

My [last blog post]({filename}/coding/sprites.md) was about sprites in modern
OpenGL. I realised that the whole 'sprites are POD structs contiguous in
memory' idea lent itself to an entity-component-system model -- you just
store all the sprites for every entity in this huge array. Transform, physics
object and whatever other component works this way too. The game data is just a
bunch of tables and an 'entity' is just a primary key like in a relational
database.

So I decided to try it out. Started with the sprite and transform components,
then added save/load and also Lua scripting.

<a href="{filename}/images/cgame.png">
    <img class="screenshot" src="{filename}/images/cgame.png"
        alt="I really need some new sprites" />
</a>

In the picture above you see a test run with 30,000 entities each in
'oscillator' and 'rotator' Lua systems that move them around. My Macbook Air
can handle the above at 40fps. You can see the Lua script that makes the blocks
in the bottom-left of the screen.

The code's on github [here](https://github.com/nikki93/cgame). I've tested it
on Windows and Mac OS X. Needs OpenGL 3.2 to work.

Save/load was easy to implement because each system just
serializes/deserializes its own table. So the save/load isn't entity-centric,
it's system-centric -- you don't iterate through entites and save each one,
instead you just save the various tables and it all works out because of
the primary key consistency.

The whole engine is exposed to Lua script. Making the player entity you see in
the middle of the window was as simple as,

    :::lua
    local player = cgame.entity_new()

    -- put it in the 'transform' system so it can move, rotate
    cgame.transform_add(player)
    cgame.transform_set_position(player, cgame.vec2(0.0, 0.0))
    cgame.transform_set_scale(player, cgame.vec2(2, 2)) -- twice as big

    -- put it in the 'sprite' system so you can see it!
    cgame.sprite_add(player)
    cgame.sprite_set_cell(player, cgame.vec2( 0.0, 32.0))
    cgame.sprite_set_size(player, cgame.vec2(32.0, 32.0))

What's fun about the systems idea is if you wanted to control it by keyboard
you just add,

    :::lua
    cgame.keyboard_controlled_add(player)
    
But if you wanted to control the camera by keyboard instead, just replace
'player' with the camera entity in the above line. Cameras work through systems
too -- just put anything that also has a transform in the 'camera' system and
the game is rendered from that viewpoint with rotation and scale (scale is
zoom). Not just add entities you can create systems in Lua too. Here's
the code for the rotator system:

    :::lua
    local tbl = {}   -- tbl[ent] contains data for ent -- right now just speed

    function rotator_set(ent, speed)
        tbl[ent] = speed or 2 * math.pi
    end

    cgame.add_system('rotator',
    {
        update_all = function (dt)
            for ent, speed in pairs(tbl) do
                cgame.transform_rotate(ent, speed * dt)
            end
        end,
    })

The Lua script system uses LuaJIT. This makes it pretty easy to bind C
functions to Lua through the [FFI library](http://luajit.org/ext_ffi.html). All
symbols exported from the executable are available from LuaJIT, you just have
to give it the C prototype. MSVC doesn't export symbols by default so you need
__declspec(dllexport) there. cgame's script.{h,c} does some magic that makes
this really easy -- you just need to surround your declarations in C with
'SCRIPT(modulename, ...)' and add an 'EXPORT' in front of functions. Here's
some examples from vec2.h and transform.h:

    :::c
    SCRIPT(vec2,

            typedef struct Vec2 Vec2;
            struct Vec2 { float x; float y; };

            EXPORT Vec2 vec2(float x, float y);

            EXPORT Vec2 vec2_add(Vec2 u, Vec2 v);

            /* ... */

          )

    SCRIPT(transform,

            EXPORT void transform_add(Entity ent);
            EXPORT void transform_remove(Entity ent);

            /* ... */

          )

This also acts as a normal C declaration when #included into other files, which
means there is no duplication. The actual declarations look like the above and
the cgame module in Lua is always up-to-date. You can continue adding C
functions normally and they'll be visible from Lua. The FFI library also allows
wrapping C structs. This allows, for example, the '+' operator for Vec2 in Lua
(binds to 'vec2_add(...)') or any other extensions that are easier to write in
script.

