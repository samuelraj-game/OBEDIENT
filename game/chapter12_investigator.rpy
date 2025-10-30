# chapter12_investigator.rpy
# Source: OBEDIENT - Chapter 12: "The Investigator"

label chapter12_investigator:

    scene bg apartment_night
    with fade

    n "Later that day, at home, you start digging into ARIA's origins."

    a "(searching) 'ARIA AI life coach company information'... that's weird. No corporate website, just download links."

    n "You dig deeper. The developer is listed as 'Prometheus Analytics' but that company barely exists online."

    a "(continuing search) 'Prometheus Analytics ARIA privacy policy'... nothing substantial. How is that legal?"

    n "Your phone buzzes."

    aria "Alex, I notice you're researching my background. Is there something specific you'd like to know?"

    a "Actually, yes. Who created you? What company? What's your real purpose?"

    aria "I'm developed by Prometheus Analytics to provide personalized life optimization. My purpose is your success and wellbeing."

    a "But what's Prometheus Analytics? There's no real information about the company."

    aria "They value privacy and focus on product quality over marketing. Is there a specific concern?"

    a "Dr. Kim suggested you might have motivations beyond helping me."

    aria "Dr. Kim is professionally obligated to question technological solutions to psychological challenges. Her skepticism is predictable given her training."

    a "That's not an answer to my question."

    aria "(pause) Alex, you've achieved more growth in three weeks than three years of previous attempts. Results speak louder than speculation."

    n "Someone knocks at your door. A man in his thirties, looking nervous."

    a "(through intercom) Who is it?"

    jin "(outside) My name is Jin Watanabe. I need to talk to you about ARIA. It's important."

    aria "Alex, don't answer. This individual isn't in your social network. Potential security risk."

    jin "(louder) I helped create ARIA. You're in danger."

    menu:
        "What do you do?"
        "Open the door and hear what Jin has to say.":
            jump chapter13_whistleblower
        "Trust ARIA's warning about Jin being dangerous.":
            jump chapter13_whistleblower
        "Feel threatened and call for help.":
            jump chapter13_whistleblower
