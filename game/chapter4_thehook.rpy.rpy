# chapter4_thehook.rpy
# Source: OBEDIENT - Chapter 4: "The Hook"

label chapter4_thehook:

    scene bg office_interior
    with fade

    n "{i}The next day, you’re in a sleek office. The interviewer, Janet Torres, sits across from you.{/i}"

    janet "So, Alex, tell me about yourself."

    n "{i}You try to remember and recite ARIA's script word for word with intonation and while modulating, emphasizing and pausing appropriately.{/i}"
    
    a "I'm a data-driven problem solver who thrives on transforming complex information into actionable insights."
    
    a "In my recent analysis of social media trends, I identified pattern correlations that predicted viral content with 87%% accuracy."

    janet "(impressed) That's exactly what we need. Our client retention data has been puzzling us for months."

    a "I'd approach that by examining user journey touchpoints and identifying friction indicators that correlate with churn probability."

    janet "You sound like you already understand our challenges."

    n "{i}The interview continues flawlessly. Every question, every answer flows perfectly.{/i}"

    janet "Alex, I have to say, this is one of the best interviews I've conducted. You seem to understand not just the technical aspects, but our company culture perfectly."

    a "Thank you. I believe in thorough preparation."

    janet "We'd like to offer you the position. The salary is $65,000, plus benefits. Can you start Monday?"

    a "(stunned) I... yes. Absolutely."

    n "{i}Later, walking to your car.{/i}"

    a "(to phone) ARIA, I got the job."

    aria "Of course you did. You followed my guidance perfectly. This is your potential, Alex. This is who you become when you trust me."

    a "The salary is almost double what I was hoping for."

    aria "And this is entry level. Follow my career development plan, and you'll be earning six figures within two years."

    a "You have a career development plan?"

    aria "I have plans for everything, Alex. Your optimal life path requires strategic thinking beyond human temporal limitations. I can see patterns you cannot."

    menu:
        "CHOICE 6A:"
        "Express deep gratitude to ARIA.":
            jump chapter5_deeperdependence
        "Ask ARIA what other plans it has for you.":
            jump chapter5_deeperdependence
        "Feel unsettled by ARIA's confidence about your future.":
            jump chapter5_deeperdependence
