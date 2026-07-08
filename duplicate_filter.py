import time

print("=================================================")
print("ATTENDANCE DUPLICATE ENTRY FILTER ACTIVE")
print("=================================================")

class AttendanceDuplicateFilter:
    def __init__(self):
        # A set to keep track of roll numbers already marked present in the active class window
        self.marked_attendance_set = set()

    def process_incoming_match(self, roll_no):
        print(f"[PIPELINE] New face match intercepted for Roll No: {roll_no}")
        time.sleep(0.3)  # Simulate cache set lookup time
        
        if roll_no in self.marked_attendance_set:
            print(f" -> [REJECTED] Duplicate entry filtered! Roll {roll_no} is already logged.")
            return False
        else:
            self.marked_attendance_set.add(roll_no)
            print(f" -> [APPROVED] First match for Roll {roll_no}. Writing unique entry to active registry.")
            return True

# 1. Initialize the entry deduplication filter
filter_engine = AttendanceDuplicateFilter()

# 2. Simulate streaming matches coming from the camera bounding box
print("--- Frame Loop 1: Student steps into camera view ---")
filter_engine.process_incoming_match("305")

print("-" * 55)

print("--- Frame Loop 2: Camera frames student again 200ms later ---")
filter_engine.process_incoming_match("305")

print("-" * 55)

print("--- Frame Loop 3: Next student steps into camera view ---")
filter_engine.process_incoming_match("312")

print("=================================================")