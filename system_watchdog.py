import time

print("=================================================")
print("SYSTEM THERMAL & PERFORMANCE WATCHDOG ACTIVE")
print("=================================================")

class SystemWatchdog:
    def __init__(self, max_cpu_threshold=85.0, max_temp_celsius=78):
        self.max_cpu = max_cpu_threshold
        self.max_temp = max_temp_celsius
        # Simulating operational machine stats under typical model inference load
        self.simulated_telemetry = [
            {"cpu_utilization": 45.2, "ram_available_gb": 9.4, "core_temp_c": 52},
            {"cpu_utilization": 88.7, "ram_available_gb": 4.1, "core_temp_c": 81}  # High stress case
        ]

    def audit_hardware_metrics(self, stats):
        print(f"[MONITOR] Inspecting local thread telemetry...")
        time.sleep(0.4)  # Simulate sensor polling interval
        
        print(f" -> Metrics: CPU Load = {stats['cpu_utilization']}% | Temp = {stats['core_temp_c']}°C | RAM Free = {stats['ram_available_gb']} GB")
        
        # Check constraints against safety bounds
        if stats["cpu_utilization"] > self.max_cpu or stats["core_temp_c"] > self.max_temp:
            print("[VERDICT: CRITICAL] Hardware limits exceeded!")
            print(" -> [ACTION] Requesting pipeline throttling or frame skip to lower thermal stress.")
            return False
        else:
            print("[VERDICT: NOMINAL] Hardware parameters safe. Processing loop operating cleanly.")
            return True

    def run_telemetry_cycles(self):
        for index, cycle in enumerate(self.simulated_telemetry, 1):
            print(f"--- Telemetry Scan Cycle #{index} ---")
            self.audit_hardware_metrics(cycle)
            print()
            time.sleep(0.3)

# 1. Initialize the monitoring system
watchdog = SystemWatchdog()
watchdog.run_telemetry_cycles()

print("=================================================")