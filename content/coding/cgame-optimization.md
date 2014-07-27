Title: cgame: 11-line optimization
Slug: cgame-optimization
Date: 2014-7-22
Summary: quick optimization with big results

I've continued to work on cgame since the independent work
deadline. Most interesting updates:

- **Backwards-compatible save for C systems:** This is more of an
  internal thing, but basically this means changing the format of C
  save/load data (by, for example, adding or removing properties) will
  not make old save files unusable.
- **Animation system:**
  [Here](https://www.youtube.com/watch?v=4LV8jJMeuRA)'s a video if it
  in use.

The focus of this blog post, however, is on a [small change](https://github.com/nikki93/cgame/commit/d2e0d17e344c02443c6139e0787490e1c2cf24d9)
I made to the code that brought a big performance bonus. C functions
of the form `x_y` are available as `cs.x.y` in Lua. This allows
writing `cs.transform.rotate(...)` for `transform_rotate(...)`, which
is the same as if transform was actually a Lua system. So Lua scripts
see a consistent API for both Lua and C systems. This was made
possible by the following Lua code:

    :::lua
    local systems_mt = {
        __index = function (t, k)
            local v = rawget(t, k)

            if v == nil then
                local mt = {
                    __index = function (_, k2)
                        return cg[k .. '_' .. k2]
                    end,
                }
                return setmetatable({}, mt)
            end
            return v
        end,
    }
    cg.systems = setmetatable({}, systems_mt)
    cs = cg.systems

So the metatable of `cs` makes it so that accessing a non-existent
member gives a table that concatenates the keys and returns the C
symbol. While reviewing the code today I realized this internal table
was being re-created every access, so I added some memoization:

    :::lua
    local system_binds = {}
    local systems_mt = {
        __index = function (t, k)
            local v = rawget(t, k)

            if v == nil then
                local bind = system_binds[k]
                if bind == nil then
                    bind = setmetatable({}, {
                        __index = function (_, k2)
                            return cg[k .. '_' .. k2]
                        end,
                    })
                    system_binds[k] = bind
                end
                return bind
            end
            return v
        end,
    }
    cg.systems = setmetatable({}, systems_mt)
    cs = cg.systems

The results? Here's a screenshot of the FPS counter when running
`test_huge.lua` with 2000 blocks before the change:

<a href="{filename}/images/cgame-optimization-before.png">
    <img class="screenshot" src="{filename}/images/cgame-optimization-before.png"
        alt="I really need some new sprites" />
</a>

And here it is after:

<a href="{filename}/images/cgame-optimization-after.png">
    <img class="screenshot" src="{filename}/images/cgame-optimization-after.png"
        alt="I really need some new sprites" />
</a>

Yup, it actually maxed out the FPS (which is capped at about 60).
