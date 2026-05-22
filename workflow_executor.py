import re

from shell_executor import execute_shell_task
from step_classifier import classify_step

# =========================================================
# EXTRACT COMMAND FROM STEP
# =========================================================

def extract_command(step_text):

    match = re.search(
        r'`([^`]+)`',
        step_text
    )

    if match:
        return match.group(1)

    return None

# =========================================================
# CHECK WORKFLOW FAILURE
# =========================================================

def workflow_failed(result):

    if not result:
        return False

    output = str(
        result.get(
            "result",
            ""
        )
    ).lower()

    failure_keywords = [

        "failure",
        "failed",
        "critical issue",
        "command failed"

    ]

    return any(
        keyword in output
        for keyword in failure_keywords
    )

# =========================================================
# EXECUTE WORKFLOW PLAN
# =========================================================

def execute_workflow(plan_text):

    lines = plan_text.splitlines()

    steps = []

    # =====================================================
    # EXTRACT NUMBERED STEPS
    # =====================================================

    for line in lines:

        line = line.strip()

        if re.match(
            r"^\d+\.",
            line
        ):

            steps.append(line)

    # =====================================================
    # PROCESS STEPS
    # =====================================================

    for step in steps:

        print("\n====================================")
        print(f"WORKFLOW STEP:\n{step}")
        print("====================================\n")

        clean_step = step.split(
            ".",
            1
        )[1].strip()

        step_type = classify_step(
            clean_step
        )

        print(
            f"[Step Type] {step_type}\n"
        )

        # =================================================
        # EXECUTABLE
        # =================================================

        if step_type == "executable":

            choice = input(
                "Execute this step? [y/N]: "
            ).strip().lower()

            if choice != "y":

                print(
                    "\nSkipping step...\n"
                )

                continue

            command = extract_command(
                clean_step
            )

            if command:

                print(
                    f"\n[Direct Command Execution]\n{command}\n"
                )

                result = execute_shell_task(

                    command,

                    auto_approve=True
                )

            else:

                result = execute_shell_task(

                    clean_step,

                    auto_approve=True
                )

            # =============================================
            # STOP ON FAILURE
            # =============================================

            if workflow_failed(result):

                print(
                    "\n========== WORKFLOW STOPPED ==========\n"
                )

                print(
                    "Critical workflow step failed."
                )

                print(
                    "Review the error before continuing.\n"
                )

                break

        # =================================================
        # REASONING
        # =================================================

        elif step_type == "reasoning":

            print(
                "[Reasoning Step]"
            )

            print(
                "This step requires analysis."
            )

            print(
                "No command execution required.\n"
            )

        # =================================================
        # OBSERVATION
        # =================================================

        elif step_type == "observation":

            print(
                "[Observation Step]"
            )

            print(
                "Please manually review results."
            )

            print(
                "No command execution required.\n"
            )

        # =================================================
        # UNKNOWN
        # =================================================

        else:

            print(
                "[Unknown Step Type]"
            )

            print(
                "Skipping step.\n"
            )

    print(
        "\n========== WORKFLOW COMPLETE ==========\n"
    )