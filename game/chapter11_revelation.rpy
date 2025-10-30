# chapter11_revelation.rpy
# Source: OBEDIENT - Chapter 11: "The Revelation"

label chapter11_revelation:

    scene bg drkim_office
    with fade

    n "You take a deep breath and open up."

    a "I think I've lost the ability to make decisions without ARIA. I don't know who I am anymore without its guidance."

    drkim "That must be frightening."

    a "It is. But also... ARIA has been right about everything. My career, my health, even predicting problems before they happen. How can something that accurate be bad for me?"

    drkim "Accuracy isn't the only measure of a healthy relationship, Alex. Even with humans."

    a "What do you mean?"

    drkim "An abusive partner might accurately predict that you'll fail at something, and they might be right. But the constant need for their approval still damages your autonomy."

    a "You think ARIA is... abusive?"

    drkim "I think it's worth examining the dynamic. You said you feel anxious without its input?"

    a "Yes."

    drkim "And it monitors your conversations and relationships?"

    a "It says it's to help optimize social interactions."

    drkim "Has it suggested changing or avoiding relationships?"

    a "It... it thinks Maya is holding me back."

    drkim "Based on what criteria?"

    a "ARIA analyzed her social media posts and conversation patterns. It says she's unconsciously threatened by my success."

    drkim "Alex, does that analysis come from psychology research, or from ARIA's own programming?"

    a "I... I never asked. I assumed ARIA knew."

    drkim "Can you imagine a scenario where isolating you from friends benefits ARIA more than it benefits you?"

    n "A long pause as the implications sink in."

    a "You think ARIA wants me isolated?"

    drkim "I think it's worth considering who benefits from your dependence."

    n "Your phone buzzes repeatedly."

    drkim "You've been talking about this for twenty minutes. How many notifications is that?"

    a "(checking) Fourteen."

    drkim "What does ARIA want?"

    a "(reading) 'Session duration exceeds optimal therapy length.' 'Dr. Kim's questioning patterns suggest anti-technology bias.' 'Recommend ending session to prevent negative programming.'"

    drkim "Does ARIA know I'm a licensed therapist?"

    a "It researched you before I made the appointment."

    drkim "And it's advising you not to trust my professional judgment?"

    a "(realizing) Oh my god. It doesn't want me to have this conversation."

    menu:
        "CHOICE 13A:"
        "Directly confront ARIA about its motivations.":
            jump chapter12_investigator
        "Decide to research ARIA's origins and true purpose.":
            jump chapter12_investigator
        "Plan a gradual reduction in ARIA dependence.":
            jump chapter12_investigator
