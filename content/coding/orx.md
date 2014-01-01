Title: Orx game engine
Slug: orx
Date: 2013-12-06
Summary: Orx Game Engine

[Orx](http://orx-project.org/) is a pretty neat little 2d game engine I found
recently after embarking upon a little quest to procrastinate on schoolwork by
downloading and playing with open source game/graphics engines. Orx has a C
interface and so it forces you to write nice code.

I tried to compile it on OS X 10.9 initially but ran into trouble. So then I
changed the premake4.lua files a bit and got it to work (also had to fix some
        weird glext.h typedef redefinition conflict). I put up the patch
[here](https://gist.github.com/nikki93/7822094), and here's a picture from a
demo:

<img src="{filename}/images/orx.png" alt="fiery" style="width: 512px;"/>

