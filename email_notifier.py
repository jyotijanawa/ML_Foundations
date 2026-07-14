import time

print("=================================================")
print("AUTOMATED EMAIL NOTIFICATION ENGINE ACTIVE")
print("=================================================")

class EmailNotificationEngine:
    def __init__(self):
        # Simulated target server endpoints
        self.smtp_server_domain = "smtp.mdu-campus.edu"
        self.sender_address = "attendance-alert@mdu.edu"

    def dispatch_attendance_alert(self, recipient_email, student_roll, course_code, attendance_rate):
        print(f"[MAIL CLIENT] Connecting to SMTP gateway: {self.smtp_server_domain}...")
        time.sleep(0.4)  # Simulate network handshake latency
        
        print(f"[TEMPLATE] Compiling dynamic text data blocks for {student_roll}...")
        
        # Formulating the email alert layout configuration
        email_body = (
            f"Subject: Attendance Alert Alert - Course {course_code}\n"
            f"To: {recipient_email}\n"
            f"From: {self.sender_address}\n\n"
            f"Dear Student,\n"
            f"This is an automated notice that your tracked record in course {course_code} "
            f"is currently logged at {attendance_rate}%. Please ensure you attend the upcoming blocks."
        )
        
        time.sleep(0.3)
        print("\n--- Dispatched Transmission Payload Preview ---")
        print(email_body)
        print("-" * 48)
        print(f"[SUCCESS] Message delivered safely to relay queue. ID: mail_tx_{student_roll}")
        return True

# 1. Initialize the communication utility
notifier = EmailNotificationEngine()

# 2. Simulate dispatching a structural compliance alert row
notifier.dispatch_attendance_alert(
    recipient_email="jyoti.student@mdu.edu", 
    student_roll="305", 
    course_code="PCC-CSE-303G", 
    attendance_rate=65.5
)

print("=================================================")