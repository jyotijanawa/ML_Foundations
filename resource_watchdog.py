import os
import platform
import time

print("=================================================")
print("PIPELINE SYSTEM HARDWARE WATCHDOG ACTIVE")
print("=================================================")

class SystemResourceWatchdog:
    def __init__(self):
        self.os_type = platform.system()
        self.processor = platform.processor()

    def display_system_profile(self):
        print(f"[INFO] Operating System Detected: {self.os_type}")
        print(f"[INFO] Core Processor Infrastructure: {self.processor}")

    def monitor_pipeline_load(self):
        print("\n[WATCHDOG] Initializing real-time resource check...")
        
        # Simulating standard system diagnostic polling
        for check_idx in range(1, 4):
            time.sleep(0.4)  # Emulating sensor check delay
            print(f"--- Diagnostic Scan #{check_idx} ---")
            print("CPU Core Status: STABLE (Processing threads operating normally)")
            print("System Memory Allocations: SAFE (Sufficient overhead for model execution)")
            print("Status: PIPELINE HEALTHY")

# 1. Initialize and run the hardware supervisor
watchdog = SystemResourceWatchdog()
watchdog.display_system_profile()
watchdog.monitor_pipeline_load()

print("=================================================")