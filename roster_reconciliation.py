import time

print("=================================================")
print("ROSTER DISCREPANCY FINDER ENGINE ACTIVE")
print("=================================================")

class RosterReconciliation:
    def __init__(self):
        # Simulated data structures from both inputs
        self.automated_camera_logs = {"301", "305", "312", "315"}
        self.manual_sheet_logs = {"301", "305", "320"}

    def scan_for_mismatches(self):
        print("[AUDIT] Cross-referencing automated datasets with manual sheets...")
        time.sleep(0.5)  # Simulate set difference calculations
        
        # Find students caught by camera but missing on paper
        camera_only = self.automated_camera_logs.difference(self.manual_sheet_logs)
        
        # Find students signed on paper but missed by the camera stream
        manual_only = self.manual_sheet_logs.difference(self.automated_camera_logs)
        
        print("\n--- Discrepancy Detection Telemetry ---")
        if not camera_only and not manual_only:
            print("[SUCCESS] Integrity Check: Logs are perfectly synchronized.")
        else:
            for roll in camera_only:
                print(f" -> [MISMATCH] Roll {roll}: Marked by CAMERA, missing on MANUAL sheet.")
            for roll in manual_only:
                print(f" -> [MISMATCH] Roll {roll}: Marked on MANUAL sheet, missing from CAMERA logs.")
                
        print("-" * 50)
        print("[STATUS] Reconciliation scan complete. Flagged anomalies isolated.")

# 1. Initialize the validation engine node
reconciler = RosterReconciliation()
reconciler.scan_for_mismatches()

print("=================================================")