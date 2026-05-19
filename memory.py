import json
import os

from datetime import datetime

MEMORY_FILE = "memory.json"

# =========================================================
# INITIALIZE MEMORY FILE
# =========================================================

def initialize_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as f:

            json.dump([], f)

# =========================================================
# LOAD MEMORY
# =========================================================

def load_memory():

    initialize_memory()

    with open(MEMORY_FILE, "r") as f:

        return json.load(f)

# =========================================================
# SAVE MEMORY
# =========================================================

def save_memory(entry):

    memory = load_memory()

    memory.append(entry)

    with open(MEMORY_FILE, "w") as f:

        json.dump(memory, f, indent=4)

# =========================================================
# CREATE MEMORY ENTRY
# =========================================================

def create_memory_entry(

    user_prompt,
    task_type,
    command=None,
    result=None

):

    entry = {

        "timestamp": str(datetime.now()),

        "task_type": task_type,

        "user_prompt": user_prompt,

        "command": command,

        "result": result
    }

    save_memory(entry)

# =========================================================
# GET RECENT MEMORIES
# =========================================================

def get_recent_memories(limit=5):

    memory = load_memory()

    return memory[-limit:]

# =========================================================
# GET RELEVANT MEMORIES
# =========================================================

def get_relevant_memories(

    current_prompt,
    limit=3

):

    memory = load_memory()

    current_prompt = current_prompt.lower()

    relevant = []

    for entry in reversed(memory):

        user_prompt = str(
            entry.get("user_prompt", "")
        ).lower()

        shared_words = set(
            current_prompt.split()
        ).intersection(

            set(user_prompt.split())
        )

        if len(shared_words) > 0:

            relevant.append(entry)

        if len(relevant) >= limit:
            break

    return list(reversed(relevant))

# =========================================================
# FORMAT RELEVANT MEMORIES
# =========================================================

def format_relevant_memories(

    current_prompt,
    limit=3

):

    memories = get_relevant_memories(
        current_prompt,
        limit
    )

    if not memories:

        return "No relevant memory."

    formatted = ""

    for memory in memories:

        formatted += f"""

Timestamp:
{memory.get('timestamp')}

Task Type:
{memory.get('task_type')}

User Prompt:
{memory.get('user_prompt')}

Result:
{memory.get('result')}

-------------------------
"""

    return formatted

# =========================================================
# GET LAST ACTION
# =========================================================

def get_last_action():

    memory = load_memory()

    if not memory:
        return "No previous actions found."

    last = memory[-1]

    return f"""
Last Action:

Task Type:
{last.get('task_type')}

User Prompt:
{last.get('user_prompt')}

Result:
{last.get('result')}
"""