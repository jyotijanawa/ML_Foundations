import time

print("=================================================")
print("DAILY ATTENDANCE ANALYTICS ENGINE MODULE ACTIVE")
print("=================================================")

class AttendanceSummaryGenerator:
    def __init__(self, course_code, total_students):
        self.course_code = course_code
        self.total_students = total_students
        self.present_records = []

    def load_mock_session_data(self):
        # Simulating data parsed from the CSV ledger for a single class session
        self.present_records = [
            {"id": "MDU-CSE-301", "name": "Amit Kumar", "time": "09:02:15"},
            {"id": "MDU-CSE-305", "name": "Priya Sharma", "time": "09:04:40"},
            {"id": "MDU-CSE-312", "name": "Rahul Verma", "time": "09:09:12"},
            {"id": "MDU-CSE-320", "name": "Sneha Gupta", "time": "09:14:55"} # Came after the 10-min window
        ]

    def generate_dashboard(self, late_threshold_mins=10):
        print(f"\n[METRICS] Generating Report for Course: {self.course_code}")
        print(f"[METRICS] Total Batch Strength: {self.total_students}")
        print("-" * 50)
        
        present_count = len(self.present_records)
        absent_count = self.total_students - present_count
        attendance_percentage = (present_count / self.total_students) * 100
        
        late_count = 0
        print("Verified Present Students:")
        for student in self.present_records:
            # Parse minutes from the timestamp string (HH:MM:SS)
            _, mins, _ = map(int, student["time"].split(":"))
            
            status_flag = ""
            if mins >= late_threshold_mins:
                status_flag = " -> [LATE ARRIVAL]"
                late_count += 1
                
            print(f" * {student['id']} | {student['name'].ljust(15)} | Logged at: {student['time']}{status_flag}")
            
        print("-" * 50)
        print(f"Total Present : {present_count}")
        print(f"Total Absent  : {absent_count}")
        print(f"Late Flags    : {late_count}")
        print(f"Attendance Rate: {attendance_percentage:.1f}%")

# 1. Initialize the analyzer for a standard class batch of 60 students
analyzer = AttendanceSummaryGenerator(course_code="PCC-CSE-304G (Advanced Java)", total_students=60)
analyzer.load_mock_session_data()
analyzer.generate_dashboard()

print("=================================================")