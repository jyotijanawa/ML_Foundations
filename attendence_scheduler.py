import datetime

print("=================================================")
print("AUTOMATED TIMETABLE PERIOD CONTROLLER ACTIVE")
print("=================================================")

class AttendanceScheduler:
    def __init__(self):
        # Define the official campus daily class timetable slots
        # Format: "Period_Name": (Start_Hour, Start_Minute, End_Hour, End_Minute)
        self.timetable = {
            "CSE-302_Compiler_Design": (9, 0, 10, 0),
            "CSE-304_Advanced_Java": (10, 15, 11, 15),
            "CSE-306_Artificial_Intelligence": (11, 30, 12, 30),
            "CSE-308_Computer_Vision_Lab": (14, 0, 15, 30)
        }
        # Allow attendance logging only during the first 10 minutes of a lecture
        self.attendance_window_minutes = 10

    def check_active_session(self, test_datetime=None):
        # Use current system time unless a specific test time is passed in
        current_time = test_datetime if test_datetime else datetime.datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        
        print(f"Current System Clock: {current_hour:02d}:{current_minute:02d}")
        
        for class_name, (sh, sm, eh, em) in self.timetable.items():
            # Check if current time falls within the overall lecture slot
            class_start = datetime.time(sh, sm)
            class_end = datetime.time(eh, em)
            check_time = current_time.time()
            
            if class_start <= check_time <= class_end:
                # Calculate how many minutes have passed since class started
                minutes_elapsed = (current_hour - sh) * 60 + (current_minute - sm)
                
                if minutes_elapsed <= self.attendance_window_minutes:
                    print(f"Active Match: {class_name}")
                    print(f"Status: CAMERA ACTIVE ({self.attendance_window_minutes - minutes_elapsed} mins remaining to mark entry)")
                    return True, class_name
                else:
                    print(f"Active Match: {class_name}")
                    print("Status: LOCKOUT (Window closed. Attendance logging expired for this period.)")
                    return False, class_name
                    
        print("Status: SYSTEM DORMANT (No academic class currently scheduled at this hour)")
        return False, None

# 1. Initialize the timetable controller
scheduler = AttendanceScheduler()

print("Simulating Morning Processing Check (9:04 AM):")
# Create a test timestamp for 09:04 AM
morning_test = datetime.datetime.now().replace(hour=9, minute=4, second=0)
scheduler.check_active_session(test_datetime=morning_test)

print("-" * 50)

print("Simulating Late Arrival Processing Check (10:45 AM):")
# Create a test timestamp for 10:45 AM
late_test = datetime.datetime.now().replace(hour=10, minute=45, second=0)
scheduler.check_active_session(test_datetime=late_test)

print("=================================================")