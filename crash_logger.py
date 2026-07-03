import time
import os

print("=================================================")
print("SYSTEM EXCEPTION LOGGER & CRASH DUMP PORTAL ACTIVE")
print("=================================================")

class CrashLogger:
    def __init__(self, log_filename="system_error.log"):
        self.log_filename = log_filename
        self.simulated_errors = [
            {"type": "CameraDeviceException", "details": "Hardware disconnect: Video input stream at index 0 lost signal pin contact."},
            {"type": "DatabaseLockError", "details": "I/O collision: 'attendance_master.db' is locked by another process thread."}
        ]

    def log_runtime_exception(self, error_type, error_details):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CRITICAL] {error_type}: {error_details}\n"
        
        print(f"[PROCESS] Intercepted runtime exception threat: {error_type}")
        print(f" -> Writing incident telemetry data to: {self.log_filename}...")
        
        # Emulating writing out to a persistent local text file block
        time.sleep(0.4)
        
        print(f"[SUCCESS] Crash dump logged cleanly. System safety state engaged.")
        print(f"+" + "-"*55 + "+")
        print(f"| Snapshot Dump: {error_type.ljust(38)} |")
        print(f"| Details: {error_details[:44].ljust(44)}... |")
        print(f"+" + "-"*55 + "+")

    def run_simulated_fault_checks(self):
        print("[DIAGNOSTIC] Initializing defensive exception tracking matrix...\n")
        
        # Loop through our mock faults to simulate catching runtime bugs
        for error in self.simulated_errors:
            self.log_runtime_exception(error["type"], error["details"])
            print()
            time.sleep(0.3)

# 1. Initialize the black box exception logging system
logger = CrashLogger()
logger.run_simulated_fault_checks()

print("=================================================")