import time

print("=================================================")
print("FACULTY VISUAL REPORT FORMATTER MODULE ACTIVE")
print("=================================================")

class FacultyReportFormatter:
    def __init__(self, subject, total_lectures):
        self.subject = subject
        self.total_lectures = total_lectures
        # Sample tracking data matching student records to total attended sessions
        self.student_attendance_history = {
            "Amit Kumar": 28,
            "Priya Sharma": 30,
            "Rahul Verma": 29,
            "Sneha Gupta": 18,  # Low attendance case
        }

    def render_faculty_dashboard(self, attendance_shortage_limit=75.0):
        print(f"\n[DASHBOARD] Attendance Overview for: {self.subject}")
        print(f"[DASHBOARD] Total Lectures Delivered: {self.total_lectures}")
        print("+" + "-"*61 + "+")
        print(f"| {'Student Name'.ljust(18)} | {'Attended'.center(10)} | {'Rate (%)'.center(10)} | {'Status'.center(12)} |")
        print("+" + "-"*61 + "+")

        shortage_alerts = []

        for student, attended in self.student_attendance_history.items():
            time.sleep(0.2)  # Emulate data rendering interval
            attendance_rate = (attended / self.total_lectures) * 100
            
            if attendance_rate < attendance_shortage_limit:
                status_str = "SHORTAGE"
                shortage_alerts.append(f" -> ALERT: {student} is below threshold ({attendance_rate:.1f}%)")
            else:
                status_str = "ELIGIBLE"
                
            print(f"| {student.ljust(18)} | {str(attended).center(10)} | {f'{attendance_rate:.1f}%'.center(10)} | {status_str.center(12)} |")

        print("+" + "-"*61 + "+")

        # Render a clear warning block if any students have an attendance shortage
        if shortage_alerts:
            print("\n!!! [WARNING] ATTENDANCE CRITICAL DEFICIT NOTIFICATION !!!")
            for alert in shortage_alerts:
                print(alert)
            print("Action Required: Please notify corresponding students regarding exam eligibility rules.")

# 1. Initialize report viewer (e.g., tracking a semester block of 32 lectures)
formatter = FacultyReportFormatter(subject="PCC-CSE-304G (Advanced Java)", total_lectures=32)
formatter.render_faculty_dashboard()

print("=================================================")