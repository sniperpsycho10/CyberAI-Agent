from models import ask_qwen

from memory import format_relevant_memories

# =========================================================
# AI INTENT CLASSIFIER
# =========================================================

def classify_prompt(user_prompt):

    recent_memory = format_relevant_memories(
        user_prompt
    )

    prompt = f"""
You are an AI intent classifier.

You also have access to relevant recent memory.

RELEVANT MEMORY:
{recent_memory}

Classify the CURRENT user request into ONLY ONE category.

Possible categories:
- shell
- coding
- reasoning

Definitions:

shell:
- Linux commands
- system operations
- docker commands
- wifi checks
- networking tasks
- cybersecurity operational tasks
- command execution

coding:
- writing code
- bash scripts
- python programs
- exploit development
- automation scripts
- tool development

reasoning:
- explanations
- theory
- conversational memory questions
- teaching
- comparisons
- asking about previous actions
- asking what happened earlier
- asking about history/context
- learning topics

IMPORTANT:
Respond with ONLY ONE WORD.

CURRENT USER REQUEST:
{user_prompt}
"""

    response = ask_qwen(prompt)

    return response.strip().lower()