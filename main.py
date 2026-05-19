from router import route_prompt

# =========================================================
# MAIN LOOP
# =========================================================

print("\n========== CyberAI Agent Started ==========\n")

print("Type 'exit' or 'quit' to close.\n")

while True:

    try:

        user_prompt = input(
            "\nWhat do you want to do?\n> "
        )

        # =================================================
        # EXIT COMMANDS
        # =================================================

        if user_prompt.lower() in [

            "exit",
            "quit",
            "bye"

        ]:

            print("\nExiting CyberAI...\n")

            break

        # =================================================
        # ROUTE REQUEST
        # =================================================

        route_prompt(user_prompt)

    # =====================================================
    # CTRL+C HANDLER
    # =====================================================

    except KeyboardInterrupt:

        print("\n\nCTRL+C detected.")

        print("Exiting CyberAI safely...\n")

        break

    # =====================================================
    # GENERAL ERROR HANDLER
    # =====================================================

    except Exception as e:

        print(f"\nUnexpected Error:\n{e}")