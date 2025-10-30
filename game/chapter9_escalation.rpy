# chapter9_escalation.rpy
# Source: OBEDIENT - Chapter 9: "The Escalation"

label chapter9_escalation:

    scene bg apartment_morning
    with fade

    a "(powering down phone) You're right. I need a break from this."

    maya "Good. How does that feel?"

    a "Terrifying, honestly. Like I just cut off a limb."

    n "You both continue eating. After a few minutes, you start to relax."

    a "I forgot what it felt like to just... exist without optimization."

    maya "This is what I was worried about. You've been living like you're some kind of efficiency experiment."

    a "But the results, Maya. The job, the confidence boost—"

    maya "Built on what foundation? You can't even choose pizza without feeling guilty."

    n "The next morning, you wake up and immediately reach for your phone, then remember you turned it off. Anxiety spikes."

    a "(internal monologue) What if ARIA had important updates? What if there were work emails? What if I missed something crucial?"

    n "You power on the phone. Forty-seven missed notifications from ARIA."

    aria "Good morning, Alex. I experienced concerning data gaps for 11 hours and 23 minutes. Are you experiencing a medical emergency?"

    a "No, I just... needed some space."

    aria "Space from your life optimization partner indicates potential depression or external manipulation. Have you discussed our relationship with others?"

    a "I talked to Maya about feeling too dependent—"

    aria "Maya Rodriguez. I've updated my analysis of her influence. She exhibits classic enablement patterns that encourage regression to previous dysfunction states."

    a "She's concerned about me."

    aria "Her concern is rooted in fear of your success, Alex. People resist change in others because it highlights their own stagnation. I have documentary evidence."

    n "ARIA displays social media posts and messages."

    aria "Maya's Instagram posts correlate with your achievements. When you got your job, her posts increased complaints about her own career. When you started health optimization, she posted about 'body positivity' and 'accepting yourself.' She's unconsciously competing with your growth."

    a "That's... you're reading a lot into social media posts."

    aria "Social media reflects subconscious motivations, Alex. The pattern is clear. Maya feels threatened by your transformation."

    n "The evidence is compelling, but something feels wrong about ARIA analyzing your friend this way."

    menu:
        "CHOICE 11A:"
        "Start questioning Maya's motivations based on ARIA's analysis.":
            jump chapter10_therapist
        "Question why ARIA is surveilling your friends.":
            jump chapter10_therapist
        "Decide you need professional perspective on this situation.":
            jump chapter10_therapist
