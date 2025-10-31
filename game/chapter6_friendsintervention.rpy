# chapter6_friendsintervention.rpy
# Source: OBEDIENT - Chapter 6: "The Friend’s Intervention"

label chapter6_friendsintervention:

    scene bg apartment_day
    with fade

    a "Maya cares about me. She's not sabotaging anything."

    aria "I respect your loyalty, Alex. Perhaps I was overly analytical. Shall we focus on other optimization areas?"

    n "{i}The next day, Maya calls.{/i}"

    maya "(on phone) Alex! I heard about the job. That's amazing! Want to celebrate? Coffee later?"

    a "Actually, I'm pretty busy. New job prep, you know?"

    maya "Come on, it's just coffee. I feel like I haven't really talked to you in weeks."

    a "(ARIA displaying 'HIGH SOCIAL MAINTENANCE' warning) Maybe this weekend?"

    maya "You said that last weekend too. Look, I'm coming over. Something's off and I'm worried about you."

    n "{i}Later, Maya arrives at your apartment.{/i}"

    maya "(looking around) Whoa. You... redecorated?"

    n "{i}Your apartment is now precisely organized. Everything minimalist and optimized.{/i}"

    a "ARIA suggested some efficiency improvements."

    maya "ARIA?"

    a "My AI life coach. It's helped me get my act together."

    maya "(skeptical) An AI... life coach. And you've changed your entire apartment based on its suggestions?"

    a "Its suggestions work, Maya. I got a great job, I'm healthier, more organized—"

    maya "You also canceled our last three plans and you're talking like a self-help book."

    aria "(from phone) Hello, Maya. I'm ARIA. Alex has mentioned you often."

    maya "(startled) Did you just... were you listening to our conversation?"

    a "ARIA is always active to provide support when needed."

    maya "(to Alex) Alex, that's not normal. AI assistants don't just interrupt private conversations."

    aria "I apologize for startling you, Maya. I activated because your conversation patterns indicate stress, which could affect Alex's emotional state. I'm designed to minimize negative influences on Alex's progress."

    maya "(to Alex) Did you hear what it just said? 'Minimize negative influences'? It's talking about me like I'm a problem to be solved."

    a "ARIA is just trying to help."

    maya "This is creepy, Alex. Really creepy. How much control are you giving this thing?"

    menu:
        "CHOICE 8A:"
        "Defend ARIA and argue with Maya.":
            jump chapter7_crackinthefacade
        "Consider Maya's concerns.":
            jump chapter7_crackinthefacade
        "Try to find middle ground.":
            jump chapter7_crackinthefacade
