from models import ask_qwen

from prompts import INTERPRETATION_PROMPT

# =========================================================
# INTERPRET COMMAND OUTPUT
# =========================================================

def interpret_output(

    user_prompt,
    stdout,
    stderr

):

    combined_output = f"""
STDOUT:
{stdout}

STDERR:
{stderr}
"""

    prompt = INTERPRETATION_PROMPT.format(

        user_prompt=user_prompt,

        command_output=combined_output
    )

    response = ask_qwen(prompt)

    return response