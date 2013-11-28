Title: nscript revived
Slug: nscript-revived
Date: 2010-10-12
Summary: nscript revived

(adapted from my old website)

In September last year, I'd written 'nscript', a simple stack based scripting
langauge interpreter. After about two days of work, I put it [on
GitHub](http://github.com/nikki93/nscript). However, it was soon forgotten as I
got busy with school work.

Recently I made a post about it on a mailing list. The post (along with
        replies) can be found
[here](http://thread.gmane.org/gmane.comp.misc.suckless/3488). Motivated by the
feedback I received, I added a lot of features to it toward the end of August.
The latest changes are available on GitHub.

In nscript, constructs like 'assignments', 'control structures', or 'function
definitions' which are usually special syntactical elements in other languages
are actually high level constructs. 'Pure nscript' itself consists only of
objects (strings, blocks, numbers), variables and the stack. Even the
assignment built-in, '=' is an executable - it simply takes a symbol and a
value.

For example, named functions can be created by assigning blocks of code to
variables. Even the assignment operator itself is a function that can be
replaced by your own.

nscript code looks like this:-

    
    :::bash
    {
        #Add last two on stack, but keep last on stack.
        rot 1 at +
        #Print sum (duplicate to keep it for next time).
        dup spacePrint
    } &_fib =

    {
        #Subtract 2 since we already print 0, 1 anyway.
        2 - &n =

        #Print first two terms.
        '0 1 ' print
        #Put first two terms.
        0 1

        #Run _fib n times.
        &_fib n repeat
    } &fib =

    25 fib

The above code prints the first 25 elements of the Fibonacci series.

In nscript, everything is an object. The code '2 3' pushes integer objects 2
and 3 onto the stack. Prepending a name with an '&' pushes a 'symbol' with that
name onto the stack. '=' takes a symbol and a value from the stack (in that
        order) and sets a 'variable' with the name of the symbol to that value.
The variable can then be accessed with that name. The following code thus sets
'two' to 2:-

    :::bash
    2 &two =

Simply a name would push the value of that variable onto the stack. 'print'
takes the last object from the stack and prints it. So, the following code
would print '2':-

    :::bash
    two print

But there's a catch - If the object referred to by the variable is
'executable', then it will be executed, instead of being pushed onto the stack.
This is why writing 'print' prints something - It runs an executable which is a
built-in object stored in a built-in variable called 'print'. There are more
other such built-ins, such as '+', '-', 'repeat' etc.

Code within { } will push that code onto the stack as a block, which is an
executable. 'repeat' takes an executable and an integer 'n' and runs the
executable n times. So, the following code prints 'Hello!' 20 times:-

    :::bash
    { "Hello!\n" print } 20 repeat

To prevent an executable variable from being executed by naming it, the name
can be prepended by '&'. This would create a symbol with that name. Execution
of a symbol means executing the variable with that name. So, the following code
prints 1 .. 10 in reverse order:-

    :::bash
    1 { dup 1 + } 9 repeat
    &print 10 repeat

Using the above constructs, what are usually called 'functions' in other
languages can be created in the following way:-

    :::bash
    { print ' ' print } &spacePrint =
    'Hello' spacePrint
    1 2 3 &spacePrint 3 repeat

Here we create a function 'spacePrint' to print something with a space after it
by assigning a block to the 'spacePrint' variable.

Structures such as 'if' or 'ifelse' which are usually keywords in other
languages are implemented simply again as executables. 'if' takes an executable
and a condition and executes the executable only if the condition is true.
'ifelse' takes two executables, and works like if, except if the condition is
false it executes the second condition. Here's an example ('getchar' pushes a
        character from standard input onto the stack):-

    :::bash
    getchar 'Y' == { "Y!" print } { "Not Y!" print } ifelse

Names need not really be alphanumeric. You can create your own '^' operator for
exponentiation this way:-

    :::bash
    {
        &p = 
        &n =

        #Put n on the stack p times, then multiply p times. We
        #also put a 1 on the stack to allow for p = 0.
        1
        { n } p repeat 
        &* p repeat
    } &^ =

    3 4 ^ print #Prints 81.

There are more concepts such as 'namespaces'. Do check out the nscript code,
      it's only about 1075 lines of C. The core itself is rather small, most
      visible functionality is implemented through built-ins.

