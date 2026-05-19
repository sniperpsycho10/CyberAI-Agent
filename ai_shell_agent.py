import ollama
import subprocess
import json

# =========================================================
# USER REQUEST
# =========================================================

user_goal = input("\nWhat do you want to do?\n> ")

# =========================================================
# AI PROMPT
# =========================================================

prompt = f"""
You are a cybersecurity Linux assistant running on Kali Linux.

The user wants:
{user_goal}

Respond ONLY with valid JSON.

Use this exact structure:

{{
  "command": "linux command here",
  "explanation": "simple beginner explanation",
  "risk": "LOW/MEDIUM/HIGH",
  "side_effects": "possible side effects",
  "recovery": "recovery instructions"
}}

Rules:
- No markdown
- No backticks
- No extra text
- Output valid JSON only
- Prefer Kali Linux compatible commands
- Avoid unnecessary sudo
- Be concise and accurate
"""

# =========================================================
# SEND TO OLLAMA
# =========================================================

response = ollama.chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    options={
    "num_predict": 120,
    "num_ctx": 2048
    }
)

ai_output = response["message"]["content"]

# =========================================================
# PARSE JSON RESPONSE
# =========================================================

try:

    data = json.loads(ai_output)

except Exception as e:

    print("\n========== JSON PARSE ERROR ==========\n")

    print("Raw AI Output:\n")
    print(ai_output)

    print(f"\nError:\n{e}")

    exit()

# =========================================================
# EXTRACT VALUES
# =========================================================

command = data.get("command", "").strip()
explanation = data.get("explanation", "").strip()
risk = data.get("risk", "").strip().upper()
side_effects = data.get("side_effects", "").strip()
recovery = data.get("recovery", "").strip()

# =========================================================
# VALIDATE COMMAND
# =========================================================

if not command:

    print("\nNo valid command found.")
    exit()

# =========================================================
# DANGEROUS COMMAND DETECTION
# =========================================================

dangerous_keywords = [

    # FILE DELETION
    "rm -rf",
    "rm -r",
    "shred",
    "wipe",

    # DISK OPERATIONS
    "mkfs",
    "fdisk",
    "parted",
    "dd ",
    "wipefs",

    # POWER CONTROL
    "shutdown",
    "reboot",
    "poweroff",
    "halt",

    # FORK BOMBS
    ":(){:|:&};:",

    # PERMISSIONS
    "chmod -R 777",
    "chmod 777",
    "chown -R",

    # FIREWALL / NETWORK
    "iptables -F",
    "iptables --flush",
    "ufw disable",
    "systemctl stop firewalld",
    "systemctl disable firewalld",
    "nft flush ruleset",
    "service networking stop",
    "systemctl stop NetworkManager",

    # PACKAGE MANAGEMENT
    "apt remove",
    "apt purge",

    # USER MANAGEMENT
    "userdel",
    "deluser",

    # PROCESS CONTROL
    "kill -9",
    "pkill",
    "killall",

    # WIFI / MONITOR MODE
    "airmon-ng start",
    "airmon-ng check kill",
    "nmcli radio wifi off",

    # ROOT ACCESS
    "sudo su",
    "sudo -i",

    # FILESYSTEM
    "mount",
    "umount",

    # REMOTE EXECUTION
    "curl | bash",
    "wget | bash",

    # REVERSE SHELLS
    "bash -i",
    "nc -e",

    # DOCKER
    "docker rm",
    "docker system prune",

    # LOGS / HISTORY
    "history -c",
]

# =========================================================
# CHECK FOR HIGH RISK COMMANDS
# =========================================================

high_risk_detected = False

for keyword in dangerous_keywords:

    if keyword in command:

        high_risk_detected = True
        break

# =========================================================
# DISPLAY AI RESPONSE
# =========================================================

print("\n========== AI GENERATED RESPONSE ==========\n")

print(f"Command:\n{command}\n")

print(f"What this does:\n{explanation}\n")

print(f"Risk Level: {risk}\n")

print(f"Possible Side Effects:\n{side_effects}\n")

print(f"Recovery Steps:\n{recovery}\n")

# =========================================================
# HIGH RISK WARNING
# =========================================================

if high_risk_detected:

    print("\n========== HIGH RISK WARNING ==========\n")

    print("This command may:")
    print("- Modify or damage the system")
    print("- Delete important files")
    print("- Disable networking")
    print("- Affect services")
    print("- Reduce security")
    print("- Require manual recovery")

    print("\nReview the command VERY carefully.\n")

    confirm = input("Type YES to continue: ").strip()

    if confirm != "YES":

        print("\nExecution cancelled.")
        exit()

# =========================================================
# NORMAL CONFIRMATION
# =========================================================

else:

    choice = input("Execute this command? [y/N]: ").strip().lower()

    if choice != "y":

        print("\nExecution cancelled.")
        exit()

# =========================================================
# EXECUTE COMMAND
# =========================================================

print("\nRunning command...\n")

try:

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    output_text = ""

    print("========== COMMAND OUTPUT ==========\n")

    if result.stdout:

        print(result.stdout)
        output_text += result.stdout

    if result.stderr:

        print("\n========== ERRORS ==========\n")
        print(result.stderr)

        output_text += "\nERRORS:\n" + result.stderr

    # =====================================================
    # AI INTERPRETATION
    # =====================================================

    print("\n========== AI INTERPRETATION ==========\n")
    # =====================================================
    # LIMIT OUTPUT SIZE FOR FASTER AI ANALYSIS
    # =====================================================

    output_text = output_text[:3000]
    analysis_prompt = f"""
You are a cybersecurity Linux mentor AI.

The following command was executed:

COMMAND:
{command}

The terminal output was:

{output_text}

Give a VERY SHORT analysis.

Include ONLY:
- success/failure
- most important finding
- critical issue if any
- one troubleshooting step if needed

Maximum 5 short bullet points.
Be concise and operational.

Be concise but educational.
"""

    analysis_response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": analysis_prompt
            }
        ],
        options={
        "num_predict": 120,
        "num_ctx": 2048
        }
    )

    analysis = analysis_response["message"]["content"]

    print(analysis)

# =========================================================
# EXECUTION FAILURE
# =========================================================

except Exception as e:

    print(f"\nExecution failed:\n{e}")
