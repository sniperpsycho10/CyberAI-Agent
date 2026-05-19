from models import ask_qwen
from models import ask_deepseek
from memory import get_last_action
from shell_executor import execute_shell_task

from classifier import classify_prompt

from memory import (
    create_memory_entry,
    format_relevant_memories
)

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
    # MEMORY QUERY HANDLER
    # =====================================================

    memory_questions = [

        "what did i do before",
        "what did i do earlier",
        "last command",
        "last action",
        "previous action",
        "history"
    ]

    if any(
        phrase in user_prompt.lower()
        for phrase in memory_questions
    ):

        print("[Router] Using Memory Retrieval\n")

        memory_response = get_last_action()

        print("\n========== MEMORY ==========\n")

        print(memory_response)

        return

    # =====================================================
    # SHELL TASKS
    # =====================================================

    if task_type == "shell":

        print("[Router] Using Operational Shell Pipeline\n")

        execution_data = execute_shell_task(
            user_prompt
        )

        create_memory_entry(

            user_prompt=user_prompt,

            task_type="shell",

            command=execution_data.get(
                "command"
            ),

            result=execution_data.get(
                "result"
            )
        )

        return

    # =====================================================
    # CODING TASKS
    # =====================================================

    elif task_type == "coding":

        print("[Router] Using DeepSeek-Coder\n")

        response = ask_deepseek(user_prompt)

        print("\n========== AI RESPONSE ==========\n")

        print(response)

        create_memory_entry(
            user_prompt=user_prompt,
            task_type="coding",
            result=response[:500]
        )

        return

    # =====================================================
    # REASONING TASKS
    # =====================================================

    elif task_type == "reasoning":

        print("[Router] Using Qwen\n")

        relevant_memory = format_relevant_memories(
            user_prompt
        )

        enhanced_prompt = f"""
You are CyberAI.

You are a cybersecurity AI assistant with memory.

You CAN remember previous interactions.

Use memory naturally when relevant.

RELEVANT MEMORY:
{relevant_memory}

CURRENT USER REQUEST:
{user_prompt}

IMPORTANT:
- If user asks about previous actions, answer using memory
- Be concise
- Be conversational
- Do not hallucinate
- Only reference memory that actually exists
"""

        response = ask_qwen(enhanced_prompt)

        print("\n========== AI RESPONSE ==========\n")

        print(response)

        create_memory_entry(
            user_prompt=user_prompt,
            task_type="reasoning",
            result=response[:500]
        )

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

        create_memory_entry(
            user_prompt=user_prompt,
            task_type="fallback",
            result=response[:500]
        )