Title: Modern OpenGL and many, many sprites
Slug: sprites
Date: 2013-12-20
Summary: Played with 'modern' OpenGL, tried instanced sprite rendering

UPDATE: I just put the code for the experiment below on
[here](https://github.com/nikki93/opengl). Needs SDL2, FreeImage, OpenGL to
work, and it's in C++11 so you'll need that too. The real experiment code is in
the 'Test' class in main.cpp, other stuff is boilerplate.

I gave in to the 'my OpenGL knowledge is old' (no more glBegin()/glEnd())
problem and decided to try things with the new vertex buffer objects. After
learning a bit about it, I realised it made so much sense for lots-of-sprites
rendering. I looked around a bit and it seemed to be a standard technique --
it's just instancing. This is especially great if all of your sprite data is
stored as POD structs contiguous in memory because then you can just dump it
all into the GPU. So after reading a few of them nifty 'modern OpenGL'
tutorials, I coded up a little demo to see how it performed.

<img class="screenshot" src="{filename}/images/sprites.png" alt="are those cookies?" />

Here you see 100,000 sprites up on screen moving around in a random fashion.
Renders at around 30fps on my little Macbook Air. Modern OpenGL is really neat
-- you just throw a bunch of data at the GPU very quickly and then make it do
what you want it to do without having to conform to a weird API of setting 'pen
color' before you 'draw a circle' or such. The GPU is all yours.

So in the above example I just have a quad mesh that's instanced a lot. Each
instance has different position and texture coordinates. The sprites are all in
an atlas texture which allows them all to be rendered with no state changes
by just varying the texcoords. I draw all the sprites with a single OpenGL draw
call (the '6' is because each quad has two triangles):

    :::cpp
    glDrawElementsInstanced(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0, num_sprites);

The vertex shader operates on each vertex of the quad for each instance. Here's
what it looks like:


    :::glsl
    #version 150

    in vec2 vertex;

    in vec2 position;
    in vec2 cell;
    in vec2 size;

    out vec2 texcoord_;

    void main()
    {
        // texcoord
        vec2 uv = vertex + vec2(0.5, 0.5);
        texcoord_ = cell + size * uv;

        // world vertex position
        vec2 worldPos = position + vertex;
        gl_Position = vec4(worldPos * vec2(0.08, 0.1066666667), 0.0, 1.0);
    }

The 'vertex' attribute varies per actual vertex, while the rest vary only per
instance. So the shader reads in slightly higher-level information (where it
        is, etc.) about the sprite and figures it out, there's no need to do
too much on the CPU with glPushTransform()/glTranslate() or such. The
corresponding fragment shader is the standard texture-sampling one.

The key part of the code is where I bind the various arrays to their buffer objects.

    :::cpp
    // get attribute locations
    GLint vertAttrib = glGetAttribLocation(program, "vertex");
    GLint posAttrib = glGetAttribLocation(program, "position");
    GLint cellAttrib = glGetAttribLocation(program, "cell");
    GLint sizeAttrib = glGetAttribLocation(program, "size");

    // ...

    // make vbo, bind vbo attributes
    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    bufferData(GL_ARRAY_BUFFER, quadVertices, GL_STATIC_DRAW);
    glVertexAttribPointer(vertAttrib, 2, GL_FLOAT, GL_FALSE, 0, 0);
    glEnableVertexAttribArray(vertAttrib);

    // make ibo, bind ibo attributes
    glGenBuffers(1, &ibo);
    glBindBuffer(GL_ARRAY_BUFFER, ibo);
    bufferData(GL_ARRAY_BUFFER, sprites, GL_DYNAMIC_DRAW);
    glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE,
            6 * sizeof(float), 0);
    glEnableVertexAttribArray(posAttrib);
    glVertexAttribDivisor(posAttrib, 1);
    glVertexAttribPointer(cellAttrib, 2, GL_FLOAT, GL_FALSE,
            6 * sizeof(float), (void *) (2 * sizeof(float)));
    glEnableVertexAttribArray(cellAttrib);
    glVertexAttribDivisor(cellAttrib, 1);
    glVertexAttribPointer(sizeAttrib, 2, GL_FLOAT, GL_FALSE,
            6 * sizeof(float), (void *) (4 * sizeof(float)));
    glEnableVertexAttribArray(sizeAttrib);
    glVertexAttribDivisor(sizeAttrib, 1);

'vbo' here is for the quad (source for just the vertex attribute) while 'ibo'
varies across sprites (position, cell and size). I should probably come up with
better names for these...

In either case, I thought that was pretty cool and I feel like it might be fun
to try and build a nice sprite library around it. And then an animation thing
(just varying texcoords, right?). Then physics, networking, sound... A
scripting layer on top.

NIH, here I come.

