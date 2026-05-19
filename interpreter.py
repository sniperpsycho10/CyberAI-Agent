from models import ask_qwen

from prompts import INTERPRETATION_PROMPT

# =========================================================
# OUTPUT INTERPRETATION
# =========================================================

def interpret_output(command, output_text):

    output_text = output_text[:3000]

    prompt = INTERPRETATION_PROMPT.format(
        command=command,
        output=output_text
    )

    return ask_qwen(prompt)