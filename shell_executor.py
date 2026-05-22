import subprocess
import json
import re

from models import ask_qwen

from prompts import (
    COMMAND_GENERATION_PROMPT
)

from interpreter import interpret_output

from safety import sanitize_command

from recovery import (
    detect_recovery_strategy
)

# =========================================================
# DIRECT COMMAND DETECTION
# =========================================================

def is_direct_command(text):

    prefixes = [

        "sudo ",
        "docker ",
        "iwconfig",
        "ip ",
        "ss ",
        "systemctl ",
        "airmon-ng ",
        "airodump-ng ",
        "timeout ",
        "cat ",
        "ls ",
        "whoami",
        "uname "
    ]

    return any(
        text.strip().startswith(prefix)
        for prefix in prefixes
    )

# =========================================================
# EXECUTE SHELL TASK
# =========================================================

def execute_shell_task(

    user_prompt,

    auto_approve=False
):

    # =====================================================
    # DIRECT COMMAND MODE
    # =====================================================

    if is_direct_command(user_prompt):

        data = {

            "command": user_prompt,

            "explanation":
            "Direct workflow command",

            "risk":
            "LOW",

            "side_effects":
            "",

            "recovery":
            ""
        }

    # =====================================================
    # AI COMMAND GENERATION MODE
    # =====================================================

    else:

        prompt = COMMAND_GENERATION_PROMPT.format(

            user_prompt=user_prompt
        )

        response = ask_qwen(prompt)

        try:

            json_match = re.search(

                r'\{.*\}',

                response,

                re.DOTALL
            )

            if not json_match:

                raise ValueError(
                    "No JSON object found."
                )

            json_text = json_match.group(0)

            data = json.loads(json_text)

        except Exception as e:

            print(
                "\n[ERROR] Failed to parse AI JSON response.\n"
            )

            print(response)

            print(f"\nParser Error:\n{e}")

            return {

                "command": None,

                "result":
                "Failed to parse AI response."
            }

    # =====================================================
    # EXTRACT DATA
    # =====================================================

    command = data.get("command", "")

    explanation = data.get(
        "explanation",
        ""
    )

    risk = data.get(
        "risk",
        "LOW"
    )

    side_effects = data.get(
        "side_effects",
        ""
    )

    recovery_steps = data.get(
        "recovery",
        ""
    )

    # =====================================================
    # SANITIZE COMMAND
    # =====================================================

    command = sanitize_command(command)

    # =====================================================
    # DISPLAY
    # =====================================================

    print(
        "\n========== AI GENERATED RESPONSE ==========\n"
    )

    print(f"Command:\n{command}\n")

    print(
        f"What this does:\n"
        f"{explanation}\n"
    )

    print(
        f"Risk Level: {risk}\n"
    )

    print(
        f"Possible Side Effects:\n"
        f"{side_effects}\n"
    )

    print(
        f"Recovery Steps:\n"
        f"{recovery_steps}\n"
    )

    # =====================================================
    # CONFIRMATION
    # =====================================================

    if not auto_approve:

        choice = input(
            "Execute this command? [y/N]: "
        ).strip().lower()

        if choice != "y":

            print(
                "\nExecution cancelled.\n"
            )

            return {

                "command": command,

                "result":
                "Execution cancelled by user."
            }

    print(
        "\nRunning command...\n"
    )

    try:

        result = subprocess.run(

            command,

            shell=True,

            capture_output=True,

            text=True,

            timeout=30
        )

        stdout = result.stdout.strip()

        stderr = result.stderr.strip()

        if stdout:

            print(
                "\n========== COMMAND OUTPUT ==========\n"
            )

            print(stdout)

        if stderr:

            print(
                "\n========== ERRORS ==========\n"
            )

            print(stderr)

            recovery_data = (
                detect_recovery_strategy(
                    stderr
                )
            )

            if recovery_data:

                print(
                    "\n========== RECOVERY ==========\n"
                )

                print(
                    f"Issue: "
                    f"{recovery_data['message']}"
                )

                print(
                    f"Suggested Fix: "
                    f"{recovery_data['solution']}"
                )

                retry = input(
                    "\nRetry with sudo? [y/N]: "
                ).lower()

                if retry == "y":

                    if command.startswith(
                        "sudo "
                    ):

                        sudo_command = command

                    else:

                        sudo_command = (
                            f"sudo {command}"
                        )

                    print(
                        "\nRunning elevated command...\n"
                    )

                    sudo_result = subprocess.run(

                        sudo_command,

                        shell=True,

                        capture_output=True,

                        text=True
                    )

                    stdout = (
                        sudo_result.stdout.strip()
                    )

                    stderr = (
                        sudo_result.stderr.strip()
                    )

                    if stdout:

                        print(
                            "\n========== SUDO OUTPUT ==========\n"
                        )

                        print(stdout)

                    if stderr:

                        print(
                            "\n========== SUDO ERRORS ==========\n"
                        )

                        print(stderr)

        interpretation = interpret_output(

            user_prompt,

            stdout,

            stderr
        )

        print(
            "\n========== AI INTERPRETATION ==========\n"
        )

        print(interpretation)

        return {

            "command": command,

            "result": interpretation
        }

    except Exception as e:

        print(
            f"\nExecution failed:\n{e}"
        )

        return {

            "command": command,

            "result": str(e)
        }