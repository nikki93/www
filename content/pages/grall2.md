Title: GraLL 2
Slug: grall2
Date: 2013-11-27
Tags: grall2
Summary: main GraLL 2 page

[Wiki](http://wiki.github.com/nikki93/grall2) |
[Flickr](http://www.flickr.com/photos/71307578@N00/sets/72157621780859002) |
[Vimeo](http://www.vimeo.com/album/126474) |
[Facebook](http://www.facebook.com/pages/GraLL-2/208594425835003) |
[GitHub](http://github.com/nikki93/grall2) 


### Download!

GraLL 2 is still under development, but playable. You can download and try the
game in its current state. Special 'work in progress' keys:
<ul>
    <li> F1, F2: Previous level, next level
    <li> F7, F8: Save/load anywhere in a level
    <li> Ctrl+O: Show options dialog
</ul>

##### Windows

[Download!](/files/grall2-12.06.26-win32.exe) (last updated: 26 June 2012)

<!-- Tools package (if you want to make your own levels): [grall2-10.1.29-tools.zip](http://dl.getdropbox.com/u/535792/Files/grall2binaries/grall2-10.1.29-tools.zip) -->

##### Linux 

[AUR Package](http://aur.archlinux.org/packages.php?ID=40547) for Arch Linux.
For other distros, you'll have to build from
[source](http://github.com/nikki93/grall2). Check the PKGBUILD file in the AUR
package for an idea of the dependencies and build process.


### Screenshots

Some screenshots of GraLL 2. The [GraLL 2 Flickr
page](http://www.flickr.com/photos/71307578@N00/sets/72157621780859002/) has a
lot more.

<a href="http://www.flickr.com/photos/71307578@N00/4372311687/" class="screenshot" title="Level 5 by nikki93, on Flickr"><img src="http://farm5.static.flickr.com/4020/4372311687_98b4793140_m.jpg" width="240" height="150" alt="Level 5"></a><a href="http://www.flickr.com/photos/71307578@N00/4373064394/" class="screenshot" title="Level 3 by nikki93, on Flickr"><img src="http://farm5.static.flickr.com/4026/4373064394_e0263ba704_m.jpg" width="240" height="150" alt="Level 3"></a>

<a href="http://www.flickr.com/photos/71307578@N00/3933089660/" class="screenshot" title="In Dimension 2 too! by nikki93, on Flickr"><img src="http://farm3.static.flickr.com/2442/3933089660_58017cecea_t.jpg" width="100" height="63" alt="In Dimension 2 too!"></a><a href="http://www.flickr.com/photos/71307578@N00/3933088812/" class="screenshot" title="Phail by nikki93, on Flickr"><img src="http://farm4.static.flickr.com/3453/3933088812_b19677b7cc_t.jpg" width="100" height="63" alt="Phail"></a><a href="http://www.flickr.com/photos/71307578@N00/4372309761/" class="screenshot" title="Level 2 by nikki93, on Flickr"><img src="http://farm5.static.flickr.com/4028/4372309761_feb217502f_t.jpg" width="100" height="63" alt="Level 2"></a><a href="http://www.flickr.com/photos/71307578@N00/4011784766/" class="screenshot" title="Level complete! by nikki93, on Flickr"><img src="http://farm3.static.flickr.com/2461/4011784766_399e1b4e49_t.jpg" width="100" height="63" alt="Level complete!"></a><a href="http://www.flickr.com/photos/71307578@N00/4119673034/" class="screenshot" title="GraLL vs. Crate by nikki93, on Flickr"><img src="http://farm3.static.flickr.com/2611/4119673034_7bdb922fdd_t.jpg" width="100" height="63" alt="GraLL vs. Crate"></a> 

### Videos

GraLL 2 in action! Only the latest videos are shown here, check out the [GraLL
2 Vimeo page](http://www.vimeo.com/album/126474 for more).

<div>
<iframe src="http://player.vimeo.com/video/25993487?portrait=0" width="400" height="225" frameborder="0"></iframe>
<iframe src="http://player.vimeo.com/video/10539723?portrait=0" width="400" height="225" frameborder="0"></iframe>
<object width="400" height="250"><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=7719023&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" /><embed src="http://vimeo.com/moogaloop.swf?clip_id=7719023&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=00ADEF&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="250"></embed></object>
</div>

The video below is a behind-the-scenes look at GraLL 2 level editing. I wrote a
plugin for Blender that allows exporting GraLL 2 levels. Python scripts for
entities in the game can be edited and attached from within Blender too.

<iframe width="400" height="225" src="http://www.youtube.com/embed/ga1eugIf2I4?list=UUm3KPfv9Pzi-5QSthoUBYbA" frameborder="0" allowfullscreen></iframe>


### Story

GraLL 1 focuses on the development of GraLL, a spherical robot created by
Gravity Systems. After GraLL 1, GraLL is stolen by Antigravity Systems, reverse
engineered and locked up in the lab. 

Help him escape! Avoid dangerous traps and use keys, teleporters, jump-pads,
crates, moving platforms, lifts and numerous other lab equipment to your
advantage as you jump between two parallel worlds and play with gravity to
make your way through Antigravity Systems' maze-like research facility.


### Technical Mumbo Jumbo

The main highlight is the scripting system. Almost everything is scriptable,
    and almost everything is exposed to script. The scripting system allows
    every instance of a particular type of GameObject to behave differently. It
    also allows for [scripted
    sequences](http://en.wikipedia.org/wiki/Scripted_sequence). In the original
    GraLL, the behaviour of every GameObject was hard-coded. Doors were opened
    with keys, Switches toggled electricity. In GraLL 2, a Switch can execute
    any piece of Python code (with is associated only with that instance) when
    switched 'on'. It could open a Door, make a platform move. In fact, it
    could even make some music play! Of course, the usual Key-Door mechanism
    and Switch-Platform mechanisms are easier to implement through 'prefabs'
    ('prefabricated' scripted objects).


If you have the Alpha build, try this:-

1. Go to Level 2.
2. Press 'Ctrl+X', then click on a Bomb.
3. Press 'F3' to open the console, then type this in (you can skip the comments):

        :::python
        # Write an 'unpaused tick' event to attach to the clicked object.
        def clicked_utick(self, elapsed):
            self.translate(Ngf.Vector3.UNIT_X * elapsed)
        # Set clicked object's 'utick' event to this function we just wrote.
        clicked.utick = clicked_utick

4. Press 'F4' to run the code.

You should see the Bomb move slowly. It's moving along the X axis. If you used
'UNIT_Y', it'd move upward. There's a lot more fun stuff possible, check out
the Wiki for a (rather-incomplete-but-it's-there) description of the Python
interface.

Another important new feature is serialisation. This allows the game state to
be saved at any point in the game. In GraLL 2, the Player is not free to
choose, however. The game is saved only when he goes through a 'Checkpoint'
object.

GraLL 2 also features a 'dimension system'. There are two 'parallel worlds' in
the same 3D position. Objects can be either in dimension 1, dimension 2, or
both. Objects can physically interact only with other objects in their
dimension. If there's a wall in dimension 1, but not 2, to go through, switch
to dimension 2 and make your way. Kind of like how you jump over a wall by
first going 'up' and then 'forward'. Here, you move 'up' in the 'dimension
switching axis' and then go forward. Of course, these differences aren't
random, they're carefully planned out by the level designer to make fun
puzzles. :-) The best way to understand this is to watch one of the videos. An
important question that arises is, what happens when the Player switches
dimensions when GraLL 2 is in a position that is occupied by an object in the
other dimension. Well, in GraLL 2, nothing happens. You hear a 'beep', and
it'll refuse to switch.

GraLL 2 also has a lot to show off in the eye-candy department. I've written
per-pixel surface shaders (normal mapping, parallax mapping implemented), and a
'glow' compositor. This makes the game look pretty cool (in my opinion), check
out the screenshots!

Some other features worth mentioning are the 'brush' system (moving platforms
        can now be of any shape and size, not just blocks), the 'records'
system (more stats for each level), better GUI, the 'options' dialog (you can
        now set controls, graphics settings etc.), the Python interpretter
console.

Users can also make their own data (levels, textures, meshes). The game simply
searches for content in the 'Content' directory under the user directory.
In-game, he can choose which level he wants to play by clicking 'Play User
Level'. The game presents a list of the user levels it found. It can also
search within .zip files, which makes it easy to play levels made by other
users. Just download the .zip, put it somewhere in your 'Content' directory,
    and that's it!

These are just features I've implemented till now. There's going to be a lot
more. Stay tuned! ;-)


