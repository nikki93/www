Title: Macrohax v2
Slug: macrohax-v2
Date: 2009-03-22
Summary: Macrohax v2

(adapted from my old website)

I've finally implemented my most feared feature: A game save/load mechanism.

This feature was something I'd always been afraid of. I would start working on
my game, and someone would say, "Your game sucks! You need save/load!", but
that would require me to redo everything I've done in a serialisable way. A
nightmare! Sure, the games had 'jump to level', but true saving and loading
would allow you to save at any point.

Now, I use boost::serialisation coupled with NGF's 'forEachGameObject' and a
'GameObjectRecord' data structure to bring you... NGF::Serialiser! Here's what
it looks like:-

    :::cpp
    NGF_SERIALISE_BEGIN(Player)
    {
        //Because NGF::GameObject doesn't know anything about your position 
        //and orientation, but gives it to you when you're created. Some 
        //GameObjects such as 'sound' might not need these.
        NGF_SERIALISE_POSITION(mNode->getPosition());
        NGF_SERIALISE_ROTATION(mNode->getOrientation());
        
        NGF_SERIALISE_AUTO(Real, mHealth);
    }

Yup, that's all you need to make the Player GameObject persistent. You just
throw that into the class definition. The 'properties' (loaded from the level
        file (which might be exported from Blender)) and the GameObject's name
are saved too. Then, you can just do this:-

    :::cpp
    //For saving.
    NGF::Serialiser::save("SaveFile");

    //For loading.
    mGameObjectManager->destroyAll();
    NGF::Serialiser::load("SaveFile");

Beautiful, isn't it? :-)

