import time

print("=================================================")
print("ATTENDANCE ALERT & NOTIFICATION DISPATCHER ACTIVE")
print("=================================================")

class AttendanceAlertDispatcher:
    def __init__(self):
        # Simulating automated message distribution channels
        self.sms_gateway_ready = True
        self.email_server_ready = True

    def dispatch_student_notification(self, student_name, roll_no, session_name):
        print(f"\n[ALERT] Preparing check-in confirmation for Roll No: {roll_no}...")
        time.sleep(0.3)  # Simulate generating template payload
        
        message_body = f"Hello {student_name}, your attendance for '{session_name}' has been successfully logged via Face ID."
        
        if self.sms_gateway_ready:
            print(f" -> [SMS DISPATCHED] To registered mobile linking Roll {roll_no}")
            print(f"    Message: \"{message_body}\"")
        return True

    def dispatch_faculty_shortage_warning(self, student_name, current_rate):
        print(f"\n[CRITICAL ALERT] Compiling attendance deficit report for Faculty...")
        time.sleep(0.4)
        
        email_body = f"Notice: Student {student_name} has fallen to an attendance rate of {current_rate}%, violating criteria thresholds."
        
        if self.email_server_ready:
            print(f" -> [EMAIL SENT] To HOD/Faculty Dashboard Portal")
            print(f"    Content: \"{email_body}\"")
        return True

# 1. Initialize the notification engine
dispatcher = AttendanceAlertDispatcher()

# 2. Simulate sending a real-time check-in confirmation receipt
print("--- Trigger 1: Real-time Check-in Log Receipt ---")
dispatcher.dispatch_student_notification("Priya Sharma", "305", "Advanced Java")

print("-" * 55)

# 3. Simulate an automated system warning flag distribution
print("--- Trigger 2: Automatic Shortage Flag Mailer ---")
dispatcher.dispatch_faculty_shortage_warning("Sneha Gupta", 56.2)

print("=================================================")