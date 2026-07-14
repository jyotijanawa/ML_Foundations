import time

print("=================================================")
print("HARDWARE UTILIZATION & DIAGNOSTICS MONITOR ACTIVE")
print("=================================================")

class SystemHealthMonitor:
    def __init__(self):
        # Setting safe performance ceilings
        self.cpu_warning_threshold = 85.0  # Percentage
        self.memory_warning_threshold = 90.0  # Percentage

        # Mocking active hardware metric tracking snapshots
        self.diagnostic_snapshots = [
            {"cpu_load": 45.2, "ram_usage": 62.5, "camera_fps": 24.1},
            {"cpu_load": 88.7, "ram_usage": 74.1, "camera_fps": 18.4},  # High CPU drop check
            {"cpu_load": 52.1, "ram_usage": 65.8, "camera_fps": 24.0}
        ]

    def evaluate_resource_health(self, snapshot, index):
        print(f"\n[DIAGNOSTIC SNAPSHOT #{index}] Querying internal system buses...")
        time.sleep(0.4)  # Simulate sampling hardware registers
        
        print(f" -> CPU Load   : {snapshot['cpu_load']}%")
        print(f" -> RAM Usage  : {snapshot['ram_usage']}%")
        print(f" -> Camera Rate: {snapshot['camera_fps']} FPS")
        
        # Check constraints against safety limits
        if snapshot["cpu_load"] > self.cpu_warning_threshold:
            print(" -> [STATUS: ALERT] High CPU thermal load detected! Scaling down thread queues.")
        elif snapshot["ram_usage"] > self.memory_warning_threshold:
            print(" -> [STATUS: ALERT] RAM capacity constraint reached! Flushing frame caches.")
        else:
            print(" -> [STATUS: HEALTHY] Performance parameters within nominal operating bounds.")

    def run_diagnostic_suite(self):
        for i, snapshot in enumerate(self.diagnostic_snapshots, start=1):
            self.evaluate_resource_health(snapshot, i)
            print("-" * 50)

# 1. Initialize the system diagnostics monitor node
monitor = SystemHealthMonitor()
monitor.run_diagnostic_suite()

print("=================================================")