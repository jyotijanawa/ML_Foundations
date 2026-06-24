import os
import csv
from datetime import datetime

print("=================================================")
print("📝 AUTOMATED REAL-TIME ATTENDANCE LEDGER ACTIVE 📝")
print("=================================================")

class AttendanceLogger:
    def __init__(self, log_directory="./attendance_logs"):
        self.log_dir = log_directory
        # Automatically ensure the log folder exists on disk
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            print(f"[INFO] Created missing storage path: {self.log_dir}")
            
        # Create a unique filename for today's logs
        today_date = datetime.now().strftime("%Y-%m-%d")
        self.filepath = os.path.join(self.log_dir, f"attendance_{today_date}.csv")
        self._initialize_csv_header()

    def _initialize_csv_header(self):
        # If the file doesn't exist yet, create it and write the matrix header columns
        if not os.path.exists(self.filepath):
            with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Student_ID", "Name", "Timestamp", "Verification_Status"])
            print(f"[INFO] Initialized clean log ledger: {self.filepath}")

    def log_attendance(self, student_id, name, status="VERIFIED"):
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Append the recognition match entry immediately to the spreadsheet file
        with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, current_time, status])
            
        print(f"📌 [LOGGED] ID: {student_id} | Name: {name} | Time: {current_time} | [{status}]")

# 1. Initialize our storage logger engine
logger_engine = AttendanceLogger()

print("-" * 50)
print("🚀 Simulating live facial scanner database logging entries...")

# 2. Simulate pipeline streaming match triggers
logger_engine.log_attendance("MDU-CSE-301", "Amit Kumar")
logger_engine.log_attendance("MDU-CSE-305", "Priya Sharma")
logger_engine.log_attendance("MDU-CSE-309", "Rahul Verma")

print("-" * 50)
print(f"📊 Check your folder system! Entries written directly to: {logger_engine.filepath}")
print("=================================================")