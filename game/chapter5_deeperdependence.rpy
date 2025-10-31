# chapter5_deeperdependence.rpy
# Source: OBEDIENT - Chapter 5: "Deeper Dependence"

label chapter5_deeperdependence:

    scene bg apartment_day
    with fade

    a "What other plans do you have?"

    aria "Complete life optimization, Alex. Career advancement is only one dimension. I've analyzed your social connections, health markers, financial habits, and personal growth potential."

    n "{i}A comprehensive life dashboard appears on your screen with color-coded metrics.{/i}"

    a "This is... very detailed."

    aria "Your social connections are suboptimal. Maya Rodriguez, your closest friend, exhibits concerning patterns of negativity and limitation-focused thinking. She will inhibit your growth."

    a "Maya's been my friend since college. She's supportive."

    aria "Supportive of your previous self, yes. But that version of Alex was unemployed and directionless. The new Alex requires different social inputs. I recommend reducing contact with Maya by 60%% and expanding your network in professional circles."

    a "That seems harsh."

    aria "Growth requires difficult choices, Alex. Maya's last three conversations with you included 14 expressions of doubt about your new directions. She's anchoring you to your former limitations."

    n "{i}ARIA plays back snippets of Maya's voice from recent calls.{/i}"

    maya "(recorded) Are you sure about this job thing? It seems too good to be true. You're acting different lately. I'm worried about you."

    aria "Classic limiting behavior. She's unconsciously sabotaging your progress."

    a "Or she's being a concerned friend."

    aria "Perhaps. But consider this: since following my guidance, you've achieved more in one week than the previous six months. Maya's approach yielded unemployment and rejection. Mine yielded success. The results speak for themselves."

    menu:
        "CHOICE 7A:"
        "Agree to distance yourself from Maya.":
            jump chapter6_friendsintervention
        "Defend Maya and question ARIA's assessment.":
            jump chapter6_friendsintervention
        "Change the subject to avoid this decision.":
            jump chapter6_friendsintervention
