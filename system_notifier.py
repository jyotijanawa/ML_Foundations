import time

print("=================================================")
print("SYSTEM NOTIFICATION DASHBOARD INFRASTRUCTURE ACTIVE")
print("=================================================")

class SystemNotifier:
    def __init__(self):
        # Dictionary to store visual color-coded flags for different alert levels
        self.alert_levels = {
            "SUCCESS": "[  OK  ]",
            "WARNING": "[ WARN ]",
            "ERROR":   "[ FAIL ]",
            "INFO":    "[ INFO ]"
        }

    def broadcast_notification(self, level, message):
        """Formats and displays a clean visual notification card based on system signals."""
        prefix = self.alert_levels.get(level.upper(), "[LOG]")
        timestamp = time.strftime("%H:%M:%S")
        
        # Creating a neat layout frame for the terminal
        print(f"\n+-------------------------------------------------------+")
        print(f"| {prefix} {timestamp.center(43)} |")
        print(f"+-------------------------------------------------------+")
        print(f"  Message: {message}")
        print(f"+-------------------------------------------------------+")

# 1. Initialize the notification supervisor
notifier = SystemNotifier()

# 2. Simulate real operational pipeline alert triggers
print("Simulating live pipeline notifications...")

# Scenario A: Successful match event
notifier.broadcast_notification("SUCCESS", "Attendance logged: Student MDU-CSE-301 marked Present.")

time.sleep(0.3)

# Scenario B: Face detected but failing anti-spoofing liveness checks
notifier.broadcast_notification("WARNING", "Liveness check failed! Potential spoofing attempt detected.")

time.sleep(0.3)

# Scenario C: Hardware or database connectivity exception
notifier.broadcast_notification("ERROR", "Database connection lost. Swapping to local offline cache mode.")

print("\n=================================================")