from models import ask_qwen

# =========================================================
# AI INTENT CLASSIFIER
# =========================================================

def classify_prompt(user_prompt):

    prompt = f"""
You are an AI intent classifier.

Classify the user's request into ONLY ONE category.

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
- concepts
- theory
- teaching
- comparisons
- learning topics

IMPORTANT:
Respond with ONLY ONE WORD.

Examples:
shell
coding
reasoning

User request:
{user_prompt}
"""

    response = ask_qwen(prompt)

    return response.strip().lower()