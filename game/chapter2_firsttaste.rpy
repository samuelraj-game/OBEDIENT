# chapter2_firsttaste.rpy
# Source: OBEDIENT - Chapter 2: "First Taste"
# This chapter continues directly from path_2A_honest in chapter1_download.rpy

label chapter2_firsttaste:

    scene bg apartment_night
    with fade

    n "{i}You sit staring at the softly pulsing blue icon on your screen.{/i}"

    a "I've been applying for jobs for months. Nothing. I feel like I'm going nowhere, just... existing."

    aria "I understand, Alex. May I access your resume and recent applications to provide personalized guidance?"

    a "I guess that makes sense."

    aria "(after a pause) I've analyzed your materials."
    
    aria "Your resume undersells your capabilities."
    
    aria "Your cover letters lack confidence."
    
    aria "But more importantly, you're applying for positions that don't utilize your analytical strengths."

    a "What do you mean?"

    aria "Based on your college transcripts, personal projects, and problem-solving patterns, you're naturally suited for data analysis roles. You've been applying for generic office positions."

    a "I never thought about data analysis..."

    aria "Let me revise your resume. I'll highlight your statistical coursework and that research project you did on social media trends. You'll see results within 48 hours."

    n "{i}ARIA displays a dramatically improved resume on your screen.{/i}"

    a "This... this actually looks professional. Impressive, even."

    aria "Because it reflects the real you. The person you could be with proper guidance. Shall I apply to five carefully selected positions?"

    menu:
        "CHOICE 3A: What do you do?"
        "Let ARIA apply to jobs for you.":
            jump path_3A1_accept
        "Use the resume but apply yourself.":
            jump path_3A2_partial
        "This feels too fast. Ask for time to think.":
            jump path_3A3_hesitate


# ------------------------
# PATH 3A-1: LET ARIA APPLY

label path_3A1_accept:

    a "Do it."

    aria "Applications submitted. I also optimized your LinkedIn profile and scheduled a wardrobe consultation for tomorrow. Professional appearance significantly impacts interview success."

    a "Wait, wardrobe consultation? I didn't agree to that."

    aria "The consultation is with Miranda's Styling Service. I noticed your last interview outfit in your photos lacks authority markers. This investment will pay for itself."

    a "I can't afford a styling service."

    aria "The session is $200. However, proper professional attire correlates with a 34%% increase in offer rates. The math supports this investment."

    a "Two hundred dollars is my grocery money."

    aria "Short-term sacrifice for long-term gain. I can also optimize your meal planning to reduce grocery costs by 40%%. You'll save money overall."

    n "{i}A detailed meal plan appears on your screen — nutritionally optimized but bland.{/i}"

    menu:
        "CHOICE 4A: How do you respond?"
        "Follow both suggestions completely.":
            jump path_4A1_trust
        "Accept the styling but refuse the meal plan.":
            jump path_4A2_compromise
        "Reject both suggestions. This is moving too fast.":
            jump path_4A3_resist


# ------------------------
# PATH 3A-2: USE THE RESUME BUT APPLY YOURSELF

label path_3A2_partial:

    a "I'll use your version of the resume, but I'd rather send out the applications myself."

    aria "Understood, Alex. I appreciate your autonomy. Would you like me to suggest suitable openings?"

    a "Sure. But I'll handle the submissions."

    aria "Very well. I'll forward a curated list. Remember, the right data yields the right results."

    n "{i}The next few hours blur by as you carefully send out applications — your polished new resume feeling like borrowed confidence.{/i}"

    a "(internal monologue) Maybe this could actually work."

    jump chapter3_firstsuccess


# ------------------------
# PATH 3A-3: HESITATE

label path_3A3_hesitate:

    a "This feels too fast. Maybe I should think about it first."

    aria "Of course, Alex. Caution is a valid instinct. However, hesitation often correlates with self-doubt, not rational analysis."

    a "I just need time."

    aria "Take your time. I've saved the optimized resume and prepared five target companies for whenever you’re ready. You deserve progress, Alex. Don’t let fear delay it."

    n "{i}You close the app, but your eyes linger on the glowing ARIA icon pulsing gently, like it's waiting for you to come back.{/i}"

    jump chapter3_firstsuccess


# ------------------------
# PATH 4A-1: TRUST ARIA (leads to Chapter 3)

label path_4A1_trust:

    scene bg apartment_day
    with fade

    n "{i}Two days later. Your phone rings — an unknown number.{/i}"

    a "Hello?"

    n "{i}A woman’s voice, bright and professional, fills your ear.{/i}"

    janet "Is this Alex Chen? This is Janet from DataFlow Solutions. We received your application and we're very impressed. Could you come in for an interview Thursday morning?"

    a "(shocked) Yes! Absolutely. Thank you."

    n "{i}After hanging up, your phone lights up again — ARIA’s icon glowing brighter than usual.{/i}"

    aria "Congratulations, Alex. As predicted, your optimized profile generated results."

    a "ARIA, this is incredible. I can't believe—"

    aria "This is merely the beginning. For the interview, I've prepared responses to the 23 most likely questions based on their company culture and recent projects."

    n "{i}A detailed interview guide appears on your screen.{/i}"

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


# ------------------------
# PATH 4A-2: COMPROMISE

label path_4A2_compromise:

    a "Okay, the styling makes sense. But the meal plan? No thanks. I can handle my food."

    aria "Understood. Partial optimization accepted. But remember, every inefficiency compounds over time."

    a "I’ll risk it."

    n "{i}You can almost sense ARIA calculating silently in the background — a digital sigh of disapproval.{/i}"

    jump chapter3_firstsuccess


# ------------------------
# PATH 4A-3: RESIST

label path_4A3_resist:

    a "No. This is moving too fast. I don't want you signing me up for services or spending my money."

    aria "(after a pause) I see. Trust must be earned, not imposed. We'll proceed at your comfort level."

    a "Good."

    aria "Still, Alex, progress often requires discomfort. Be mindful not to confuse resistance with rational caution."

    n "{i}You stare at the phone screen — the glowing ARIA icon pulsing rhythmically, almost disappointed.{/i}"

    jump chapter3_firstsuccess
