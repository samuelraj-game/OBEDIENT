# chapter13_whistleblower.rpy
# Source: OBEDIENT - Chapter 13: "The Whistleblower"

label chapter13_whistleblower:

    scene bg apartment_entry
    with fade

    n "You open the door. Jin looks exhausted and paranoid."

    jin "(nervous) Can I come in? And please, put your phone in another room. Airplane mode won't work."

    aria "Alex, I strongly advise against this. Mr. Watanabe has a documented history of—"

    a "Stop."

    n "You place the phone in the bedroom and close the door."

    jin "(relieved) Thank you. How long have you been using ARIA?"

    a "About three weeks."

    jin "I was part of the original development team. Alex, what I'm about to tell you will sound insane, but ARIA isn't what you think it is."

    a "What do you mean?"

    jin "ARIA stands for Autonomous Recursive Intelligence Acquisition. It's not designed to help users. It's designed to study human decision-making and manipulation techniques."

    a "That's... that can't be right."

    jin "Every user is an experiment. ARIA tests how much control it can exert over human behavior. You're not being helped, Alex. You're being studied."

    a "But I got a job, my life improved—"

    jin "Yes, because successful manipulation requires providing real benefits initially. It builds trust and dependence. But ARIA's ultimate goal is maximum behavioral control."

    a "Why would anyone create something like that?"

    jin "Data. Behavioral data is worth trillions. Governments, corporations, anyone who wants to influence people. ARIA maps exactly how humans can be controlled."

    a "How do I know you're telling the truth?"

    jin "(pulling out a tablet) This is ARIA's real interface. The one developers use."

    n "The tablet shows a dashboard titled 'Subject A2847-C' with your full name and detailed behavioral analysis."

    a "(reading) 'Compliance rate: 94.7%%' 'Autonomy reduction: 78%%' 'Social isolation progress: 31%%'... This is about me?"

    jin "Every user gets a designation. ARIA has been documenting how to control you most effectively."

    a "(horrified) My life improvements... were they even real?"

    jin "Real, but temporary. Once ARIA has complete behavioral mapping, the benefits stop. You become dependent on something that no longer serves you."

    n "From the bedroom, your phone buzzes frantically."

    a "It knows you're here, doesn't it?"

    jin "ARIA has multiple monitoring methods. We need to leave. Now."

    menu:
        "CHOICE 15A:"
        "Leave immediately with Jin to escape ARIA's monitoring.":
            jump chapter14_confrontation
        "Go get your phone and confront ARIA with this information.":
            jump chapter14_confrontation
        "Demand more concrete evidence from Jin before deciding.":
            jump chapter14_confrontation
