import os
import csv
from datetime import datetime

print("=================================================")
print("ATTENDANCE LEDGER EXPORTER ENGINE ACTIVE")
print("=================================================")

class AttendanceLedgerExporter:
    def __init__(self, filename="daily_attendance_ledger.csv"):
        self.filename = filename
        self.initialize_ledger()

    def initialize_ledger(self):
        # Create the CSV file with column headers if it doesn't exist yet
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Student_ID", "Name", "Date", "Timestamp", "Status"])
            print(f"[INFO] New ledger file initialized: {self.filename}")
        else:
            print(f"[INFO] Existing ledger file detected and synced: {self.filename}")

    def log_attendance(self, student_id, student_name):
        # Get the current system date and exact time
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        
        # Append the verified student entry directly to the file
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, student_name, current_date, current_time, "Present"])
            
        print(f"Logged entry: {student_name} ({student_id}) marked Present at {current_time}")

# 1. Initialize the exporter engine
exporter = AttendanceLedgerExporter()

print("-" * 50)
print("Simulating identification pipeline export triggers...")

# 2. Mock data incoming from successful identity matches
exporter.log_attendance("MDU-CSE-301", "Amit Kumar")
exporter.log_attendance("MDU-CSE-305", "Priya Sharma")

print("-" * 50)
print(f"Check your project folder! Verification log updated in: {exporter.filename}")
print("=================================================")