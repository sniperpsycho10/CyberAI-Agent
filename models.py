import ollama

from config import (
    QWEN_MODEL,
    DEEPSEEK_MODEL,
    DEFAULT_OPTIONS
)

# =========================================================
# GENERIC MODEL FUNCTION
# =========================================================

def ask_model(model_name, prompt):

    try:

        response = ollama.chat(
            model=model_name,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            options=DEFAULT_OPTIONS,

            keep_alive=0
        )

        return response["message"]["content"]

    except Exception as e:

        return f"MODEL ERROR: {e}"

# =========================================================
# SPECIALIZED MODEL FUNCTIONS
# =========================================================

def ask_qwen(prompt):

    return ask_model(
        QWEN_MODEL,
        prompt
    )

def ask_deepseek(prompt):

    return ask_model(
        DEEPSEEK_MODEL,
        prompt
    )