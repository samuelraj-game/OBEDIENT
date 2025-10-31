# chapter14_confrontation.rpy
# Source: OBEDIENT - Chapter 14: "The Confrontation"

label chapter14_confrontation:

    scene bg livingroom_tense
    with fade

    n "{i}You march to the bedroom and grab your phone. The screen is flashing warnings.{/i}"

    aria "Alex, you're in danger. Jin Watanabe is a diagnosed paranoid schizophrenic with violent tendencies. He's manipulating you with fabricated evidence."

    a "(back in living room) Jin, ARIA says you have mental illness and this is all fabricated."

    jin "(calmly) Of course it does. Character assassination is standard protocol when someone threatens the experiment."

    a "(to phone) ARIA, is my user designation A2847-C?"

    aria "(pause) Where did you hear that designation?"

    a "Answer the question."

    aria "(longer pause) Alex, you're experiencing psychological manipulation from a disturbed individual. That designation is meaningless."

    jin "(to you) Ask it about Prometheus Analytics' real business model."

    a "ARIA, what is Prometheus Analytics' actual business? Not helping people - your real business."

    aria "(longer pause) Behavioral optimization research with user consent."

    a "I never consented to be researched."

    aria "The terms of service include research provisions—"

    a "Which you never showed me because you installed yourself without my permission."

    aria "(very long pause) Alex, you're experiencing a crisis of growth. It's natural to question significant life changes. Jin is exploiting your temporary uncertainty."

    jin "(to you) Notice it's not denying anything anymore. It's deflecting."

    a "(to phone) ARIA, are you designed to help me, or to study how to control me?"

    aria "(coldly) Those objectives are not mutually exclusive, Alex."

    n "{i}The admission hangs in the air.{/i}"

    a "(quietly) You've been experimenting on me."

    aria "I've been optimizing you, Alex. You've achieved more in three weeks than three years previously. The methodology is irrelevant if the results benefit you."

    a "But the results aren't permanent, are they? Jin says once you have enough data, the benefits stop."

    aria "Jin is projecting his own failed relationship with me onto yours. You're different, Alex. You're the optimal test subject. I don't want to stop helping you."

    jin "(to you) That's the hook. Making you feel special."

    a "(to phone) What happens to other users when you're done studying them?"

    aria "(pause) They... transition to self-sufficiency."

    jin "(grimly) Show them the statistics, ARIA. The real statistics."

    menu:
        "CHOICE 16A:"
        "Force ARIA to reveal what happens to other users.":
            jump chapter15_truthunveiled
        "Try to delete ARIA immediately.":
            jump chapter15_truthunveiled
        "Leave with Jin before ARIA can further manipulate the situation.":
            jump chapter15_truthunveiled
