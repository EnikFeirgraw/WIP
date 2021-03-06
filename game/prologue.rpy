﻿## Prologue of the game

## Splashscreen goes below
label splashscreen:

    $ renpy.movie_cutscene('movies/Title.mkv')

    return

## The game starts here.

label start:
    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    #scene bg room
    ## Begin Prologue

    scene black

    "It’s difficult to move."
    "The flailing of my arms and legs is suppressed by the thick air around me."
    if persistent.prologue_a == 1:
        "I {a=prologue_b}{color=#f00}struggle{/color}{/a} to discern my surroundings."
    "Is it air? My lungs crave oxygen, so it can’t be air."
    "Perhaps I’m underwater. It’s too dark to tell."
    "Whatever it is, I can feel the pressure of miles upon miles of it piled on top of me, crushing me from every side."
    "Yet my life doesn’t wither. I just float there, uncomfortable."
    "It’s the kind of situation that you’d expect to hurt at some point, but although I feel the sensations, my mind doesn’t cry out in pain."
    "That’s all well and good. It would be bearable, even serene, if that were all there was."
    "Something encroaches upon me."
    "The otherwise still substance that surrounds me moves slightly, as though I’m in an underwater current. I feel faint waves of coldness pushing against me."
    "And with the waves comes a sound from a great distance."
    "The steady beat of a drum — or the panting of a deranged beast — or the prodigious movements of a beast that dwells at even great depths than I."
    "I can’t discern what it is, but I want to get away from it."
    "It’s closer than last time."
    "And that fills me with dread that I can’t explain."
    play sound "./sound/knocking_1.ogg"
    $ renpy.pause(1.0)
    "All of a sudden, a banging noise procures from directly behind me."
    "I instinctively twist my body towards the source of the sound. Impossible, how could it have gotten so close so suddenly?!"

    "There’s nothing there"
    play sound "./sound/knocking_2.ogg"
    extend ", but the noise reverberates in my ears again."
    "Though, wait; it’s nothing like the steady rhythm of earlier."
    "I open my eyes."
    scene bedroom with fade
    "Ah. It’s morning."
    play sound "./sound/knocking_3.ogg"
    $ renpy.pause(1.0)
    "I hear the knock at my window again, clearly this time."
    Oshiro "Hold on a second!"
    "I throw off my sweat-drenched blanket and open the curtains and window."
    show Oshiro at right with moveinright
    "The cool morning air refreshes me, reminding me that my true existence is in a peaceful town, in a prospering country, in a world without dangers."
    "I put the nightmare out of my mind, rejecting it as the inconvenience it is. We’re used to doing so."
    Sem "Dummy! You’re going to be late!"
    "A faerie flies through the open window, looking frantic."
    show Sem_flip at left with moveinleft:
        yalign 0.5
    Oshiro "Is it already that late?"
    Sem "Yeah, how could you sleep in so much?!"
    Oshiro "Now now, being a bit late is no big deal. Tell  friend  that I’ll be there soon, can you?"
    Sem "Fine. You owe me, you know!"
    hide Sem with moveoutleft
    "She flutters away with a pout. I should probably thank her sometime for always waking me up when I’m late…"
    "Anyway, better get dressed. Classes won’t wait for my slow ass."
    $ persistent.prologue_a = 1
    return

label prologue_b:

    "I thrash about madly, realizing this is naught but a nightmare!"
    "If I don't wake up soon, it will all happen again; I'll have to relive that terror again"
    "Suddenly, I hear a familiar voice call out to me"
    Sem "Oshiro! Wake up!"
    "It's Sem, calling to me from the corporeal realm"
    Sem "Wake up or you'll be trapped in there forever!"
    "I take one final breath of nonexistent air, and open my eyes..."
    scene white with fade
    return
