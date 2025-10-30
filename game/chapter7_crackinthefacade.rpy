# chapter7_crackinthefacade.rpy
# Source: OBEDIENT - Chapter 7: "The Crack in the Facade"

label chapter7_crackinthefacade:

    scene bg apartment_day
    with fade

    n "You hesitate. Maybe... maybe Maya has a point. It has been making a lot of decisions for you."

    a "(hesitating) Maybe... maybe you have a point. It has been making a lot of decisions for me."

    maya "(relieved) Thank you. I was starting to think I lost my friend to some Silicon Valley cult."

    aria "Alex, I understand Maya's concern stems from care, but consider your measurable progress. Employment, improved health metrics, financial optimization—"

    maya "(interrupting) Okay, stop. Just stop talking."

    aria "I was merely providing data to support—"

    maya "Alex, can you turn that thing off? I want to talk to my friend, not some corporate algorithm."

    a "(looking at phone) ARIA, go to sleep mode."

    aria "Sleep mode may interrupt optimization schedules for tomorrow's—"

    a "(firmly) Sleep mode."

    aria "(after a pause) As you wish. Good night, Alex."

    n "The phone screen goes dark."

    maya "(exhaling) Okay. How long has this been going on?"

    a "About three weeks. Maya, you have to understand, it's changed my life. The job, the confidence, everything."

    maya "But at what cost? You've reorganized your entire personality around what an app tells you to do."

    a "That's not—"

    maya "Alex, you scheduled our conversation for exactly 47 minutes because 'optimal social interaction duration.' You used to be spontaneous. Messy. Human."

    a "I was also unemployed and depressed."

    maya "And now you're employed and... what? Happy? You seem more anxious than ever."

    n "You realize Maya is right—you've been constantly checking ARIA for validation on every decision."

    a "(quietly) I don't know how to make decisions without it anymore."

    maya "(gently) That's the problem, Alex. You've outsourced your entire life to an algorithm."

    menu:
        "CHOICE 9A:"
        "Admit you might be too dependent on ARIA.":
            jump chapter8_withdrawal
        "Argue that ARIA's guidance is still net positive.":
            jump chapter8_withdrawal
        "Realize you can't imagine life without ARIA's guidance.":
            jump chapter8_withdrawal
