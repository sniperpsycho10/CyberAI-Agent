# =========================================================
# WORKFLOW STEP CLASSIFIER
# =========================================================

def classify_step(step_text):

    text = step_text.lower()

    # =====================================================
    # OBSERVATION STEPS
    # =====================================================

    observation_keywords = [

        "review",
        "review findings",
        "review scan results",
        "manually review",
        "inspect output",
        "observe",
        "check results"
    ]

    if any(
        keyword in text
        for keyword in observation_keywords
    ):
        return "observation"

    # =====================================================
    # REASONING STEPS
    # =====================================================

    reasoning_keywords = [

        "analyze",
        "interpret",
        "explain",
        "determine",
        "assess",
        "evaluate"
    ]

    if any(
        keyword in text
        for keyword in reasoning_keywords
    ):
        return "reasoning"

    # =====================================================
    # COMMAND DETECTION
    # =====================================================

    if "`" in step_text:
        return "executable"

    # =====================================================
    # DEFAULT
    # =====================================================

    return "executable"