import json
import subprocess

from models import ask_qwen

from prompts import COMMAND_GENERATION_PROMPT

from safety import (
    sanitize_command,
    is_high_risk
)

from interpreter import interpret_output

# =========================================================
# GENERATE COMMAND
# =========================================================

def generate_command(user_prompt):

    prompt = COMMAND_GENERATION_PROMPT.format(
        user_prompt=user_prompt
    )

    response = ask_qwen(prompt)

    try:

        data = json.loads(response)

        return data

    except Exception:

        print("\nJSON PARSE ERROR\n")

        print(response)

        return None

# =========================================================
# EXECUTE SHELL TASK
# =========================================================

def execute_shell_task(user_prompt):

    data = generate_command(user_prompt)

    if not data:
        return

    command = data.get("command", "")

    command = sanitize_command(command)

    explanation = data.get("explanation", "")
    risk = data.get("risk", "")
    side_effects = data.get("side_effects", "")
    recovery = data.get("recovery", "")

    print("\n========== AI GENERATED RESPONSE ==========\n")

    print(f"Command:\n{command}\n")

    print(f"What this does:\n{explanation}\n")

    print(f"Risk Level: {risk}\n")

    print(f"Possible Side Effects:\n{side_effects}\n")

    print(f"Recovery Steps:\n{recovery}\n")

    # =====================================================
    # HIGH RISK WARNING
    # =====================================================

    if is_high_risk(command):

        print("\n========== HIGH RISK WARNING ==========\n")

        print("This command may:")
        print("- Modify the system")
        print("- Affect networking")
        print("- Delete files")
        print("- Require recovery")

        confirm = input("\nType YES to continue: ")

        if confirm != "YES":

            print("\nExecution cancelled.")

            return

    else:

        choice = input(
            "Execute this command? [y/N]: "
        ).lower()

        if choice != "y":

            print("\nExecution cancelled.")

            return

    # =====================================================
    # EXECUTE COMMAND
    # =====================================================

    print("\nRunning command...\n")

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output_text = ""

        print("========== COMMAND OUTPUT ==========\n")

        if result.stdout:

            print(result.stdout)

            output_text += result.stdout

        if result.stderr:

            print("\n========== ERRORS ==========\n")

            print(result.stderr)

            output_text += "\nERRORS:\n" + result.stderr

        interpretation = interpret_output(
            command,
            output_text
        )

        print("\n========== AI INTERPRETATION ==========\n")

        print(interpretation)

    except Exception as e:

        print(f"\nExecution failed:\n{e}")