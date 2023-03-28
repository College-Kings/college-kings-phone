label message_test:
    play ambience Room_Night fadein 2

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_1w # TPP MC (neutral, MC) lies in his bed sleeping, room in darkness.
    else:
        scene ep2s1b_1a # TPP MC (neutral, MC) lies in his bed sleeping, room in darkness.
    with dissolve

    pause 0.75

    python:
        MessengerService.new_message(amber, "A good mystery is a lot like a beautiful dame")
        MessengerService.new_message(amber, "she may be as pretty as a blossoming rose, smell sweet as spring lilacs")
        MessengerService.new_message(amber, "But roses have thorns and lilacs might have")
        MessengerService.new_message(amber, "uh...")
        MessengerService.new_message(amber, "bees inside of them?")
        MessengerService.new_message(amber, "The Big Wolf came to me with a looker of a case, like some canary in a real knock-out evening gown, gams all the way up, too tempting to pass up")
        MessengerService.new_message(amber, "What's the college's angle on the frats?")

    play sound "audio/sounds/vibrate.mp3"

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_2w # TPP Same shot, near his head his phone lights up and buzzes.
    else:
        scene ep2s1b_2a # TPP Same shot, near his head his phone lights up and buzzes.
    with dissolve

    pause 1.5

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_3w # TPP Same shot, MC (neutral, MC opens and rubs his eyes blearily, sitting up.
    else:
        scene ep2s1b_3a # TPP Same shot, MC (neutral, MC opens and rubs his eyes blearily, sitting up.
    with dissolve

    u "(Ugh, what time is it? I gotta piss.)"

    $ MessengerService.new_message(amber, "Anyone with two eyes and half a brain could see something's going on")
    play sound "audio/sounds/vibrate.mp3"

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_4w # TPP MC sits up and glances at his phone, still lit up and buzzing.
    else:
        scene ep2s1b_4a # TPP MC sits up and glances at his phone, still lit up and buzzing.
    with dissolve

    $ MessengerService.new_message(amber, "But just like that beautiful dame, trouble might lurk under the surface, just out of sight")

    pause 1.5

    $ MessengerService.new_message(amber, "Truth, as a great master once said, is not found on the mountain-top, but in the valleys where we seek her, probing and teasing til she moans like a pro skirt")
    play sound "audio/sounds/vibrate.mp3"
     
    if mc.frat == Frat.WOLVES:
        scene ep2s1b_5w # TPP MC disappears from the frame. Sound of toilet flushing, phone is still lit up and buzzing.
    else:
        scene ep2s1b_5a # TPP MC disappears from the frame. Sound of toilet flushing, phone is still lit up and buzzing.
    with dissolve

    pause 1.5

    play sound "audio/sounds/flush.mp3"

    pause 1.25

    python:
        ep2s1b_reply_clean = MessageBuilder(amber)
        ep2s1b_reply_clean.new_message("come on dude, u know i'm livin that straight edge life")
        ep2s1b_reply_clean.new_message("I don't know why, no wonder people do drugs, being sober fucking sucks")

        ep2s1b_reply_not_clean = MessageBuilder(amber)
        ep2s1b_reply_not_clean.new_message("Just pot, the normal amount!!! Come on Watson!!")
        ep2s1b_reply_not_clean.new_message("Detective Amber and her trusty sidekick have a new case!!!!!! Be a little more excited")

        ep2s1b_reply_2a_1 = MessageBuilder(amber)
        ep2s1b_reply_2a_1.add_function(reputation.add_point, RepComponent.TROUBLEMAKER)
        ep2s1b_reply_2a_1.add_reply("only reason I'm seeing this is because I slammed a couple beers with the guys when I got home and just got up to pee")
        ep2s1b_reply_2a_1.new_message("Detective amber found her trusty sidekick lost at the bottom of the bottle, mind clouded by political turmoil of earlier in the evening, the vote to end all votes")

        ep2s1b_reply_2b_1 = MessageBuilder(amber)
        ep2s1b_reply_2b_1.add_function(reputation.add_point, RepComponent.BRO)
        ep2s1b_reply_2b_1.new_message("obvs not if ur texting")
        ep2s1b_reply_2b_1.add_reply("also have no idea what a pro skirt is, is that athleisurewear?")
        ep2s1b_reply_2b_1.new_message("A pro skirt! A lady of the night! A good time gal!")
        
        MessengerService.new_message(amber, "Doesn't that sound kind of hot? Come on!!!!!!", Reply("so how stoned are you?", ep2s1b_reply_clean if v1_amber_clean else ep2s1b_reply_not_clean))
        MessengerService.add_replies(amber,
            Reply("Amber... it's 2 a.m., too many exclamation marks", ep2s1b_reply_2a_1),
            Reply("I am excited, but I'm also asleep", ep2s1b_reply_2b_1)
        )
        MessengerService.add_reply(amber, "GOODNIGHT AMBER")
        MessengerService.new_message(amber, "NO WAIT")
        MessengerService.new_message(amber, "gumshoe TLDR: Chris came to me and asked me to investigate something")

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_6w # TPP MC walks back into the frame, phone still lit up and buzzing.
    else:
        scene ep2s1b_6a # TPP MC walks back into the frame, phone still lit up and buzzing.
    with dissolve

    pause 1.25

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_7w # TPP MC flops onto his bed and reaches for his phone.
    else:
        scene ep2s1b_7a # TPP MC flops onto his bed and reaches for his phone.
    with dissolve
    
    u "(Goddamnit, it's so late. Who's sending me so many texts?)"

    python:
        if mc.frat == Frat.WOLVES:
            MessengerService.add_reply(amber, "Chris")
            MessengerService.add_reply("who is sleeping like 2 doors down from me")
            MessengerService.add_reply("Why didnt he just talk to me himself????")

        else:
            MessengerService.add_reply(amber, "Why didnt he just talk to me himself????")
            MessengerService.add_reply(amber, "I know I'm an ape but we're not on bad terms")

        MessengerService.new_message(amber, "He said he was worried you'd do more weird CSI roleplaying if he asked you directly")
        MessengerService.new_message(amber, "plus I think he wants to get on this")
        MessengerService.add_reply(amber, "Fair enuf")
        MessengerService.new_message(amber, "so wat do you say, my handsome assistant?")

        if mc.detective == Detective.PROFESSIONAL:
            MessengerService.new_message(amber, "can detective amber count on the watson to her sherlock?")

        elif mc.detective == Detective.PSYCHOLOGIST:
            MessengerService.new_message(amber, "will this detective be able to count on the incredible mental powers of her mind-bending psychologist sidekick??")

        else:
            MessengerService.new_message(amber, "will I be able to rely on my bad cop, my loose cannon, my table smashing, mercurial, shoot first and ask questions later psycho of a partner??????")

        ep2s1b_reply_3a_1 = MessageBuilder(amber)
        ep2s1b_reply_3a_1.add_function(reputation.add_point, RepComponent.TROUBLEMAKER)
        ep2s1b_reply_3a_1.set_variable("ep2s1_mc_not_into_detective", True)
        ep2s1b_reply_3a_1.add_reply("I'm exhausted from the vote")
        ep2s1b_reply_3a_1.add_reply("And the nora investigation took a lot of time, I had to frickin drive out into the middle of nowhere, it was expensive!!")
        ep2s1b_reply_3a_1.new_message("Believe me, when you hear about the case ur going to want to be part of this")
        ep2s1b_reply_3a_1.add_reply("Maybe you gotta sweeten the pot a little, whats in it for watson?")
        ep2s1b_reply_3a_1.new_message("You palooka, i'll sweeten ur deal")
        ep2s1b_reply_3a_1.new_message("images/ep2/Scene 1b/ep2s1b_detective_amber.webp")
        ep2s1b_reply_3a_1.add_reply("Consider it sweetened")
        ep2s1b_reply_3a_1.new_message("The detective's lustful sidekick was a man like any other")
        ep2s1b_reply_3a_1.new_message("Sometimes all it takes is a carrot on a stick... in this case he made the decision with both his carrot and his stick, but they were one in the same")
        ep2s1b_reply_3a_1.new_message("Rendezvu at the agency, first thing")
        ep2s1b_reply_3a_1.new_message("I'll have a fresh pot of coffee on")
        ep2s1b_reply_3a_1.new_message("And I wanna see more hustle, Watson, none of this i'm too sleepy shit")
        ep2s1b_reply_3a_1.new_message("we'll get you as hopped up on bean juice as we need to")
        ep2s1b_reply_3a_1.add_reply("GOODNIGHT AMBER")
        ep2s1b_reply_3a_1.new_message("Better make it happen or the only sleepin you'll be doin is with the fishes, pal")

        ep2s1b_reply_3b_1 = MessageBuilder(amber)
        ep2s1b_reply_3b_1.add_function(reputation.add_point, RepComponent.BRO)
        ep2s1b_reply_3b_1.add_reply("never been more excited about anything in my life")
        ep2s1b_reply_3b_1.add_reply("So excited I think I might pass out")
        ep2s1b_reply_3b_1.add_reply("ZZZZZZZZZZZZZZZZZ")
        ep2s1b_reply_3b_1.new_message("the hapless sidekick wriggled like a worm on the end of the hook")
        ep2s1b_reply_3b_1.new_message("He was in a real jam, he had stakes in the game, and no gumshoe wants to be the one to stick his fingers inside pandora's box and wiggle them around and make her moan like a 3 dollar whore")
        ep2s1b_reply_3b_1.add_reply("That took a turn half way through there")
        ep2s1b_reply_3b_1.add_reply("But yeah, obvs in")
        ep2s1b_reply_3b_1.add_reply("But only if you let me go back to sleep")
        ep2s1b_reply_3b_1.add_reply("right now")
        ep2s1b_reply_3b_1.new_message("You got urself a deal, pal!!")
        ep2s1b_reply_3b_1.new_message("Rendezvu at the agency, first thing")
        ep2s1b_reply_3b_1.new_message("I'll have a fresh pot of coffee on")

        replies = [Reply("Yes, so excited", ep2s1b_reply_3b_1)]
        if not config_censored:
            replies.append(Reply("I am once again reminding you it is 2am, which is too early for this shit", ep2s1b_reply_3a_1))

        MessengerService.add_replies(amber, *replies)

    while MessengerService.has_replies(amber):
        call screen phone
        if MessengerService.has_replies(amber):
            u "(I should reply to Amber.)"

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_8w # TPP MC (neutral, MC) is laying back on his bed, eyes drooping closed.
    else:
        scene ep2s1b_8a # TPP MC (neutral, MC) is laying back on his bed, eyes drooping closed.
    with dissolve

    pause 1

    if mc.frat == Frat.WOLVES:
        scene ep2s1b_9w # TPP MC (neutral, eyes closed) passes out, phone still in his hand.
    else:
        scene ep2s1b_9a # TPP MC (neutral, eyes closed) passes out, phone still in his hand.
    with dissolve

    pause 1

    scene sleep_transition_fast # Ignore animation
    with fade

    pause 2.2
    
    scene black
    with dissolve
    
    pause

    return
