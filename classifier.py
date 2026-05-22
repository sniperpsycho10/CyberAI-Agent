from models import ask_qwen

from memory import format_relevant_memories

# =========================================================
# FAST RULE-BASED CLASSIFICATION
# =========================================================

def local_classification(user_prompt):

    text = user_prompt.lower()

    shell_keywords = [

        "docker",
        "container",
        "network",
        "interface",
        "wifi",
        "wlan",
        "airmon",
        "airodump",
        "scan",
        "monitor mode",
        "ip address",
        "ports",
        "service",
        "process",
        "systemctl",
        "journalctl",
        "ping",
        "route",
        "firewall",
        "iptables",
        "ufw",
        "nmap",
        "whoami",
        "uname",
        "disk",
        "memory",
        "cpu"
    ]

    coding_keywords = [

        "write code",
        "python script",
        "python program",
        "bash script",
        "shell script",
        "java",
        "c++",
        "javascript",
        "exploit",
        "tool",
        "automation",
        "program"
    ]

    reasoning_keywords = [

        "explain",
        "what is",
        "how does",
        "teach me",
        "difference between",
        "compare",
        "why",
        "history",
        "what did i do before",
        "last action",
        "previous action"
    ]

    if any(
        keyword in text
        for keyword in coding_keywords
    ):
        return "coding"

    if any(
        keyword in text
        for keyword in reasoning_keywords
    ):
        return "reasoning"

    if any(
        keyword in text
        for keyword in shell_keywords
    ):
        return "shell"

    return None

# =========================================================
# AI INTENT CLASSIFIER
# =========================================================

def classify_prompt(user_prompt):

    local_result = local_classification(
        user_prompt
    )

    if local_result:
        return local_result

    recent_memory = format_relevant_memories(
        user_prompt
    )

    prompt = f"""
You are an AI intent classifier.

RELEVANT MEMORY:
{recent_memory}

Classify into ONLY ONE category:

shell
coding
reasoning

CURRENT USER REQUEST:
{user_prompt}

Respond with ONLY ONE WORD.
"""

    response = ask_qwen(prompt)

    return response.strip().lower()