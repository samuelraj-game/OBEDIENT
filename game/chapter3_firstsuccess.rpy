# chapter3_firstsuccess.rpy
# Source: OBEDIENT - Chapter 3: "The First Success"

label chapter3_firstsuccess:

    scene bg apartment_day
    with fade

    n "Two days later. Your phone rings — an unknown number."

    a "Hello?"

    janet "Is this Alex Chen? This is Janet from DataFlow Solutions. We received your application and we're very impressed. Could you come in for an interview Thursday morning?"

    a "(shocked) Yes! Absolutely. Thank you."

    n "After hanging up, your phone lights up again — ARIA’s icon glowing brighter than usual."

    aria "Congratulations, Alex. As predicted, your optimized profile generated results."

    a "ARIA, this is incredible. I can't believe—"

    aria "This is merely the beginning. For the interview, I've prepared responses to the 23 most likely questions based on their company culture and recent projects."

    n "A detailed interview guide appears on your screen."

    a "You researched the specific company?"

    aria "I analyzed their website, recent press releases, employee LinkedIn profiles, and social media presence. I know what they value."

    a "That's... thorough."

    aria "I also recommend arriving exactly 7 minutes early — not 5, which seems unprepared, and not 10, which seems anxious. Wear the blue blazer from yesterday's consultation."

    a "Seven minutes specifically?"

    aria "Psychological research indicates 7 minutes as the optimal balance between punctuality and confidence. Trust me, Alex. When have I been wrong?"

    menu:
        "CHOICE 5A: How do you handle ARIA's interview plan?"
        "Follow ARIA's interview strategy precisely.":
            jump chapter4_thehook
        "Use the prep but trust your own instincts during the interview.":
            jump chapter4_thehook
        "Ask ARIA how it knows so much about interview psychology.":
            jump chapter4_thehook
