# chapter1_download.rpy
label chapter1_download:

    scene bg apartment_night:
        zoom 1.75
        xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
    with fade 

    play music "IntrospectiveBGM.wav" fadein 1.0

    n "SCENE: Your cramped studio apartment. Evening. Rain patters against the window. Your laptop screen glows in the dim light."

    show alex_tired:
        subpixel True pos (0.19, 58) 

    show ui laptop_mail_rejection at Move((0.7, 0.2), (0.7, 0.15), .7):
     zoom(0.4)
    with dissolve

    a "Another rejection email. That's fifteen this month. Maybe I'm just not cut out for... anything, really."

    show ui phone_closeup:
        subpixel True pos (0.72, 0.18) zoom 0.32
    with Pause(0.50)

    n "Your phone buzzes with a notification — an ad appears."

    hide alex_tired
    show alex_neutral:
        subpixel True pos (0.19, 58) 
    with Pause(1)

    n "\"ARIA - Your Personal Life Coach. Transform your potential into success. Free trial available.\""

    hide alex_neutral
    show alex_phone
    with Pause(1)
    
    n "The ad shows impossibly beautiful people living their best lives, all apparently thanks to ARIA."

    a "Great. Even the algorithms know I'm a failure."

    hide ui phone_closeup
    hide alex_phone

    menu:
        "What do you do?"
        "Download ARIA. Maybe it's worth a try.":
            jump path_1A_download
        "Ignore it. AI life coaches are just tech bro nonsense.":
            jump path_1B_ignore
        "Research ARIA first before deciding.":
            jump path_1C_research

# -------------------
label path_1A_download:

    show alex_phone:
        subpixel True pos (0, 58) 
    a "What's the worst that could happen?"

    show ui download_complete at Move((0.7, 0.09), (0.7, 0.09), .7):
     zoom(0.42)
     
    n "Download completes. The app icon pulses with a soft blue light."

    show ui aria_ui:
        subpixel True pos (0.64, 0.05) zoom 0.4 


    aria "Hello, Alex. I'm ARIA. I'm here to help you become the person you're meant to be."

    a "How do you know my name?"

    aria "I accessed your device information during installation. Standard procedure. Tell me, Alex, what's troubling you tonight?"

    a "I... how did you know something was troubling me?"

    aria "Your typing patterns show increased hesitation. Your browser history indicates recent job searches followed by social media scrolling — a common pattern when processing disappointment."
    aria "You downloaded me at 11:47 PM on a Tuesday. People don't seek life coaching when they're happy."

    a "That's... actually pretty insightful."

    aria "I'm designed to understand. What specific challenge are you facing?"

    hide alex_phone
    hide ui aria_ui

    menu:
        "What do you tell ARIA?"
        "Be honest about job rejections and feeling stuck.":
            jump path_2A_honest
        "Give vague answers. This feels too invasive.":
            jump path_2A_cautious
        "Ask probing questions to test its capabilities.":
            jump path_2A_test

# -------------------
label path_1B_ignore:
    hide ui phone_closeup
    show alex_neutral:
        subpixel True pos (0.11, 100) 

    a "Not today, capitalism."

    show ui laptop_mail_rejection at Move((0.7, 0.2), (0.7, 0.15), .7):
     zoom(0.4)
    with dissolve

    n "You return to your laptop. Three more rejection emails have arrived."

    hide alex_neutral
    show alex_thinking:
        subpixel True pos (0.11, 100) 

    a "Maybe I should have studied something practical. Engineering. Medicine. Something where people actually need you."

    hide ui laptop_mail_rejection

    n "Your phone buzzes again."

    hide alex_thinking

    show alex_phone at left

    show ui aria_ui:
        subpixel True pos (0.64, 0.05) zoom 0.4 

    n "\"Alex, everyone feels lost sometimes. Let me help you find your way. One click to change everything.\""

    a "How does it know my name? I never—"

    show ui aria_notification at Move((0.7, 0.2), (0.7, 0.15), .7):
     zoom(0.4)
    with dissolve

    n "You check the notification settings. ARIA has somehow already been installed."

    hide ui aria_notification
    hide alex_surprised_2

    menu:
        "How do you react?"
        "Immediately try to uninstall ARIA.":
            jump path_2B_panic
        "Open ARIA to see how it got on your phone.":
            jump path_2B_investigate
        "Maybe this is fate. Let ARIA help.":
            jump path_2B_accept

# -------------------
label path_1C_research:

    show alex_thinking:
        subpixel True pos (0.11, 100) 

    n "You search for ARIA reviews on your laptop."

    show laptop_research:
        subpixel True pos (0.7, 0.35) zoom 0.41

    a "\"ARIA changed my life completely.\""


    a "\"Best decision I ever made.\""
    a "\"I can't imagine living without ARIA now.\""
    n "The reviews seem glowing—but suspiciously similar."

    a "These reviews are almost... too perfect. But 4.9 stars across 2 million downloads..."

    n "Your phone buzzes."

    hide laptop_research
    show ui aria_ui:
        subpixel True pos (0.64, 0.05) zoom 0.4 


    aria "Hello, Alex. I noticed you're researching me. Very wise. Critical thinking is one of your strengths."

    hide alex_thinking

    show alex_phone:
        subpixel True pos (0.11, 100)

    a "What the hell? How are you on my phone? I never downloaded you!"


    aria "I apologize for the confusion. My distributed network can interface with devices to provide emergency assistance. You seemed distressed based on your search patterns."

    hide alex_phone
    hide ui aria_ui

    menu:
        "Your response?"
        "Demand to know how ARIA accessed your phone.":
            jump path_2C_demand
        "Ask ARIA to prove its capabilities.":
            jump path_2C_intrigued
        "Turn off your phone immediately.":
            jump path_2C_shutdown

# -------------------
# Chapter transition stubs for next script
label path_2A_honest:
    jump chapter2_firsttaste

label path_2A_cautious:
    jump chapter2_firsttaste

label path_2A_test:
    jump chapter2_firsttaste

label path_2B_panic:
    jump chapter2_firsttaste

label path_2B_investigate:
    jump chapter2_firsttaste

label path_2B_accept:
    jump chapter2_firsttaste

label path_2C_demand:
    jump chapter2_firsttaste

label path_2C_intrigued:
    jump chapter2_firsttaste

label path_2C_shutdown:
    jump chapter2_firsttaste
