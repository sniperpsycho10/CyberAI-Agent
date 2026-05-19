# =========================================================
# COMMAND SANITIZATION
# =========================================================

def sanitize_command(command):

    replacements = {

        "top": "top -b -n 1",

        "ping ": "ping -c 4 ",

        "tail -f": "tail -n 20",

        "watch ": "timeout 10 ",

        "tcpdump": "timeout 10 tcpdump",

        "airodump-ng": "timeout 20 airodump-ng"
    }

    for original, replacement in replacements.items():

        if command.startswith(original):

            command = command.replace(
                original,
                replacement,
                1
            )

    return command

# =========================================================
# DANGEROUS COMMAND DETECTION
# =========================================================

dangerous_keywords = [

    "rm -rf",
    "mkfs",
    "dd ",
    "shutdown",
    "reboot",
    "poweroff",
    "chmod -R 777",
    "iptables -F",
    "ufw disable",
    "systemctl stop",
    "systemctl disable",
]

# =========================================================
# HIGH RISK DETECTION
# =========================================================

def is_high_risk(command):

    for keyword in dangerous_keywords:

        if keyword in command:
            return True

    return False