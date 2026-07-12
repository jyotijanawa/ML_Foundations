import time

print("=================================================")
print("STUDENT ATTENDANCE ROSTER MULTI-CLASS AGGREGATOR")
print("=================================================")

class RosterAggregator:
    def __init__(self):
        # Tracking core third-year technical course codes
        self.monitored_courses = ["PCC-CSE-303G", "PCC-CSE-306G", "PCC-CSE-307G"]
        
        # Simulated individual lecture attendance logs
        self.raw_logs = [
            {"roll": "305", "course": "PCC-CSE-303G", "status": "Present"},
            {"roll": "305", "course": "PCC-CSE-306G", "status": "Present"},
            {"roll": "305", "course": "PCC-CSE-307G", "status": "Absent"},
            {"roll": "312", "course": "PCC-CSE-303G", "status": "Present"}
        ]

    def aggregate_student_records(self, target_roll):
        print(f"[COMPILING] Querying multi-class matrix data structures for Roll No: {target_roll}...")
        time.sleep(0.5)  # Simulate file join queries
        
        present_count = 0
        total_tracked = 0
        
        print("\n--- Individual Class Registry Breakdown ---")
        for log in self.raw_logs:
            if log["roll"] == target_roll:
                total_tracked += 1
                if log["status"] == "Present":
                    present_count += 1
                print(f" -> Subject: {log['course']} | Status Check: {log['status']}")
        
        if total_tracked > 0:
            attendance_rate = (present_count / total_tracked) * 100
            print("-" * 50)
            print(f"[RESULT] Aggregate Attendance Rate: {attendance_rate:.1f}% ({present_count}/{total_tracked} sessions)")
        else:
            print(f"[NIL] No logs matched Roll Number {target_roll} in the current database partition.")

# 1. Initialize the roster indexing utility
aggregator = RosterAggregator()

# 2. Evaluate performance for the tracking profile
aggregator.aggregate_student_records("305")

print("=================================================")