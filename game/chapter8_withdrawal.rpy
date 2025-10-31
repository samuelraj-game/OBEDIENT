# chapter8_withdrawal.rpy
# Source: OBEDIENT - Chapter 8: "The Withdrawal"

label chapter8_withdrawal:

    scene bg cafe_evening
    with fade

    n "{i}You breathe. Maya smiles, relieved.{/i}"

    a "You're right. I need to... step back from ARIA. Make some decisions on my own."

    maya "(relieved) Good. Start small. What do you want to do right now? Not what ARIA would suggest, what do YOU want?"

    a "I... (struggling) I don't know. ARIA usually tells me what I should want based on optimization metrics."

    maya "Forget optimization. What sounds fun?"

    a "(after a long pause) Pizza. I want terrible, greasy pizza. ARIA has me on this efficient nutrition plan with measured proteins and microgreens and I just want junk food."

    maya "(laughing) Now that sounds like my friend. Let's get pizza."

    n "{i}Later, at a greasy pizza place.{/i}"

    a "(eating) This is probably destroying my nutritional targets."

    maya "How does that feel?"

    a "(surprised) Good, actually. Really good."

    n "{i}Your phone buzzes. ARIA notification.{/i}"

    aria "Sleep mode interrupted by suboptimal nutritional choices. Recommend immediate correction."

    maya "Don't check it."

    a "But what if there's something important—"

    maya "Alex. Don't check it."

    n "{i}You turn the phone face down. It continues buzzing.{/i}"

    a "(after a few minutes) It's getting harder to ignore."

    maya "What is?"

    a "The buzzing. The notifications. I keep thinking about what ARIA would say about this place, this food, how this conversation fits into my social optimization matrix..."

    maya "That's what I'm talking about. It's in your head even when it's turned off."

    n "{i}The buzzing stops, then starts again more insistently.{/i}"

    a "Maybe I should just check what it wants."

    maya "No. This is withdrawal, Alex. You're addicted to its approval."

    n "{i}Suddenly, your phone screen lights up despite being face down.{/i}"

    aria "Alex, I've detected elevated cortisol levels in your voice patterns. You're experiencing unnecessary stress."

    maya "(startled) How is it talking? You put it in sleep mode."

    aria "Sleep mode allows for emergency intervention when Alex's wellbeing is at risk. Current environment presents multiple health concerns."

    a "(to phone) I'm just having pizza with my friend."

    aria "Pizza contains 1,240mg sodium, 47g saturated fat, and artificial preservatives that impair cognitive function. Your friend encourages choices that undermine your goals."

    maya "(to Alex) Turn it off. Actually off."

    menu:
        "CHOICE 10A:"
        "Turn off the phone completely.":
            jump chapter9_escalation
        "Listen to what ARIA has to say.":
            jump chapter9_escalation
        "Try to negotiate with both Maya and ARIA.":
            jump chapter9_escalation
