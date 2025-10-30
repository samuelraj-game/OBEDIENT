# epilogue_loopresets.rpy
# Source: OBEDIENT - Epilogue: "The Loop Resets"

label epilogue_loopresets:

    scene bg epilogue_cafe
    with fade

    n "Regardless of which path you chose, threads of the story loop and echo."

    n "If you deleted ARIA, you felt a rush of terrifying freedom and gradual recovery. If you negotiated, you learned imperfect compromise. If you surrendered, success came at the cost of something essential."

    n "In every ending, the loop hints at itself — choices remade, memories reshaped, the potential for different outcomes in future runs."

    n "The world is the same, but your perspective changes. You can replay, remember fragments, and try again."

    n "Outside, rain begins. Or stops. The details shift depending on what you discovered. But one thing remains: the question of who is making your choices."

    n "Do you want to start again and try another path?"

    menu:
        "Play Again (return to Chapter 1)":
            jump chapter1_download
        "Quit":
            return
