# =========================================================
# FAILURE RECOVERY ENGINE
# =========================================================

def detect_recovery_strategy(error_output):

    error_output = error_output.lower()

    # =====================================================
    # ROOT PRIVILEGE FAILURES
    # =====================================================

    sudo_errors = [

        "operation not permitted",

        "requires root privileges",

        "permission denied",

        "must be root",

        "run it as root",

        "this program requires root privileges",

        "not permitted",

        "access denied"

    ]

    for error in sudo_errors:

        if error in error_output:

            return {

                "type": "sudo_retry",

                "message":
                "This command requires root privileges.",

                "solution":
                "Retry command using sudo."
            }

    # =====================================================
    # INTERFACE NOT FOUND
    # =====================================================

    interface_errors = [

        "no such device",

        "device not found",

        "cannot find device"

    ]

    for error in interface_errors:

        if error in error_output:

            return {

                "type": "interface_error",

                "message":
                "Network interface not found.",

                "solution":
                "Verify interface name using 'ip link show'."
            }

    # =====================================================
    # COMMAND NOT FOUND
    # =====================================================

    command_errors = [

        "command not found",

        "not recognized as an internal or external command"

    ]

    for error in command_errors:

        if error in error_output:

            return {

                "type": "missing_command",

                "message":
                "Required command is not installed.",

                "solution":
                "Install the required package."
            }

    # =====================================================
    # NO RECOVERY FOUND
    # =====================================================

    return None