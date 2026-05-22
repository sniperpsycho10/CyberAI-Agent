from models import ask_qwen

# =========================================================
# CYBERSECURITY WORKFLOW TEMPLATES
# =========================================================

WIFI_KEYWORDS = [

    "wifi",
    "wireless",
    "monitor mode",
    "wlan",
    "airodump",
    "airmon",
    "handshake"
]

DOCKER_KEYWORDS = [

    "docker",
    "container",
    "containers"
]

ENUM_KEYWORDS = [

    "enumerate",
    "enumeration",
    "audit linux",
    "linux machine",
    "system audit"
]

NETWORK_KEYWORDS = [

    "network audit",
    "audit network",
    "network configuration"
]

# =========================================================
# WIFI WORKFLOW
# =========================================================

def wifi_plan():

    return """
1. Verify wireless adapter using `iwconfig`
2. Enable monitor mode using `sudo airmon-ng start wlan0`
3. Verify monitor interface using `iwconfig`
4. Scan nearby networks using `sudo timeout 20 airodump-ng wlan0mon`
5. Review scan results
"""

# =========================================================
# DOCKER RECON
# =========================================================

def docker_plan():

    return """
1. List running containers using `docker ps`
2. List installed images using `docker images`
3. Inspect docker networks using `docker network ls`
4. Inspect running containers using `docker inspect`
5. Review findings
"""

# =========================================================
# LINUX ENUMERATION
# =========================================================

def linux_enum_plan():

    return """
1. Check kernel version using `uname -a`
2. Check current user using `whoami`
3. List users using `cat /etc/passwd`
4. Check listening ports using `ss -tulpn`
5. Check running services using `systemctl list-units --type=service`
6. Review findings
"""

# =========================================================
# NETWORK AUDIT
# =========================================================

def network_audit_plan():

    return """
1. Display interfaces using `ip a`
2. Display routes using `ip route`
3. Check DNS configuration using `cat /etc/resolv.conf`
4. Check active connections using `ss -tunap`
5. Review findings
"""

# =========================================================
# FALLBACK AI PLANNER
# =========================================================

def ai_plan(user_prompt):

    prompt = f"""
You are an expert cybersecurity workflow planner.

Create a short operational workflow.

Rules:
- Numbered steps only
- Linux/Kali focused
- Use correct commands
- Use sudo where required
- Include verification steps
- Include review/analyze steps
- English only

USER REQUEST:
{user_prompt}
"""

    return ask_qwen(prompt)

# =========================================================
# MAIN ENTRYPOINT
# =========================================================

def generate_plan(user_prompt):

    text = user_prompt.lower()

    # =====================================================
    # WIFI WORKFLOW
    # =====================================================

    if any(
        keyword in text
        for keyword in WIFI_KEYWORDS
    ):

        return wifi_plan()

    # =====================================================
    # DOCKER WORKFLOW
    # =====================================================

    if any(
        keyword in text
        for keyword in DOCKER_KEYWORDS
    ):

        return docker_plan()

    # =====================================================
    # ENUMERATION WORKFLOW
    # =====================================================

    if any(
        keyword in text
        for keyword in ENUM_KEYWORDS
    ):

        return linux_enum_plan()

    # =====================================================
    # NETWORK AUDIT
    # =====================================================

    if any(
        keyword in text
        for keyword in NETWORK_KEYWORDS
    ):

        return network_audit_plan()

    # =====================================================
    # FALLBACK
    # =====================================================

    return ai_plan(user_prompt)