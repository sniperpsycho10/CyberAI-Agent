from models import ask_qwen
from models import ask_deepseek

from shell_executor import execute_shell_task

from classifier import classify_prompt

# =========================================================
# AI-POWERED TASK ROUTER
# =========================================================

def route_prompt(user_prompt):

    # =====================================================
    # AI CLASSIFICATION
    # =====================================================

    task_type = classify_prompt(user_prompt)

    print(f"\n[Classifier] Detected: {task_type}\n")

    # =====================================================
    # SHELL TASKS
    # =====================================================

    if task_type == "shell":

        print("[Router] Using Operational Shell Pipeline\n")

        execute_shell_task(user_prompt)

        return

    # =====================================================
    # CODING TASKS
    # =====================================================

    elif task_type == "coding":

        print("[Router] Using DeepSeek-Coder\n")

        response = ask_deepseek(user_prompt)

        print("\n========== AI RESPONSE ==========\n")

        print(response)

        return

    # =====================================================
    # REASONING TASKS
    # =====================================================

    elif task_type == "reasoning":

        print("[Router] Using Qwen\n")

        response = ask_qwen(user_prompt)

        print("\n========== AI RESPONSE ==========\n")

        print(response)

        return

    # =====================================================
    # FALLBACK
    # =====================================================

    else:

        print("[Router] Unknown classification.")

        print("[Router] Falling back to Qwen.\n")

        response = ask_qwen(user_prompt)

        print("\n========== AI RESPONSE ==========\n")

        print(response)