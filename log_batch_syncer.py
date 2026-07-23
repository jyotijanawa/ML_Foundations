import time

print("=================================================")
print("ASYNC ATTENDANCE LOG BATCH SYNCER ACTIVE")
print("=================================================")

class AttendanceBatchSyncer:
    def __init__(self, batch_size_threshold=3):
        self.batch_size_threshold = batch_size_threshold
        self.event_buffer = []

    def log_detection_event(self, roll_number, confidence_score):
        timestamp = time.strftime("%H:%M:%S")
        event_payload = {
            "roll": roll_number,
            "confidence": confidence_score,
            "timestamp": timestamp
        }
        self.event_buffer.append(event_payload)
        print(f"[BUFFER] Queued detection event for Roll {roll_number} ({confidence_score:.2f}) at {timestamp}")
        
        # Check if buffer satisfies auto-flush threshold
        if len(self.event_buffer) >= self.batch_size_threshold:
            self.flush_batch_to_database()

    def flush_batch_to_database(self):
        if not self.event_buffer:
            print("[SYNC] Buffer is empty. Skipping flush sequence.")
            return

        print(f"\n[SYNC] Threshold reached ({len(self.event_buffer)} items). Initializing DB bulk commit...")
        time.sleep(0.5)  # Simulate I/O network payload latency
        
        print("--- Executing Asynchronous Bulk Insertion ---")
        for idx, record in enumerate(self.event_buffer, start=1):
            print(f" -> [{idx}/{len(self.event_buffer)}] Writing Record: Roll {record['roll']} | Conf: {record['confidence']} | Time: {record['timestamp']}")
            time.sleep(0.1)

        print("-" * 50)
        print(f"[SUCCESS] {len(self.event_buffer)} record(s) committed safely to master table.")
        self.event_buffer.clear()
        print("[STATUS] Event queue buffer reset to 0.")

# 1. Instantiate the batch synchronization manager
syncer = AttendanceBatchSyncer(batch_size_threshold=3)

print("\n--- Simulating Live Ingestion Stream ---")
# 2. Simulate streaming detection events from the main vision pipeline
syncer.log_detection_event(roll_number="301", confidence_score=0.94)
time.sleep(0.2)
syncer.log_detection_event(roll_number="305", confidence_score=0.89)
time.sleep(0.2)
syncer.log_detection_event(roll_number="312", confidence_score=0.97)  # Triggers automatic batch flush

print("=================================================")