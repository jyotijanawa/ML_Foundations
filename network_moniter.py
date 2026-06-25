import socket
import time

print("=================================================")
print("NETWORK CONNECTIVITY RESILIENCY WATCHDOG ACTIVE")
print("=================================================")

class NetworkMonitor:
    def __init__(self, target_host="8.8.8.8", port=53, timeout=2):
        self.target_host = target_host
        self.port = port
        self.timeout = timeout
        self.local_cache = []

    def check_connection(self):
        """Checks connection by opening a fast socket connection to a reliable server."""
        try:
            # Setting up a quick socket handshake
            socket.setdefaulttimeout(self.timeout)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_host, self.port))
            sock.close()
            return True
        except OSError:
            return False

    def process_attendance_sync(self, student_id, student_name):
        """Determines whether to sync directly online or cache locally."""
        print(f"\n[PING] Checking server link status for: {student_name}...")
        
        if self.check_connection():
            print("Status: ONLINE. Direct pipeline cloud sync successful!")
            # If there are cached students from a previous dropout, push them now
            if self.local_cache:
                print(f"[ALERT] Flushing cached entries to cloud database: {self.local_cache}")
                self.local_cache.clear()
        else:
            print("Status: OFFLINE. Network drop detected!")
            print(f"[WARNING] Securely archiving entry '{student_id}' to offline local memory cache.")
            self.local_cache.append({"id": student_id, "name": student_name, "time": time.strftime("%H:%M:%S")})

# 1. Initialize network supervisor
monitor = NetworkMonitor()

# 2. Simulate standard operational pipeline checks
print("--- Scenario A: Normal Operations ---")
monitor.process_attendance_sync("MDU-CSE-301", "Amit Kumar")

print("-" * 50)

# 3. Simulate an intentional timeout block by targeting an unreachable connection configuration
print("--- Scenario B: Simulating Offline Drop ---")
broken_monitor = NetworkMonitor(target_host="192.0.2.1", timeout=1)  # Invalid non-routable IP block
broken_monitor.process_attendance_sync("MDU-CSE-305", "Priya Sharma")

print("=================================================")