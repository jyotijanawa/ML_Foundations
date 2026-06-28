import csv
import os
import time

print("=================================================")
print("DAILY LEDGER CSV EXPORT ENGINE ACTIVE")
print("=================================================")

class AttendanceLedgerExporter:
    def __init__(self, course_code):
        self.course_code = course_code
        self.export_filename = f"attendance_{course_code.lower().replace('-', '_')}.csv"
        # Sample internal queue data captured by the camera stream
        self.raw_attendance_queue = [
            {"roll_no": "301", "name": "Amit Kumar", "status": "Present", "timestamp": "09:02:14"},
            {"roll_no": "312", "name": "Rahul Verma", "status": "Present", "timestamp": "09:09:12"},
            {"roll_no": "305", "name": "Priya Sharma", "status": "Present", "timestamp": "09:04:40"},
        ]

    def export_to_csv(self):
        print(f"[PROCESS] Sorting records sequentially by Roll Number...")
        # Sort records by roll number so the final spreadsheet is neat and readable
        sorted_records = sorted(self.raw_attendance_queue, key=lambda x: x["roll_no"])
        
        print(f"[PROCESS] Generating structural ledger file: {self.export_filename}...")
        time.sleep(0.5)  # Simulate file creation delay
        
        # Write out to a standard tabular comma-separated structure
        try:
            with open(self.export_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write file headers
                writer.writerow(["Course Code", "Roll No", "Student Name", "Status", "Log Time"])
                
                # Write student data rows
                for record in sorted_records:
                    writer.writerow([self.course_code, record["roll_no"], record["name"], record["status"], record["timestamp"]])
                    print(f" -> Exported: Roll No {record['roll_no']} | {record['name']}")
                    
            print(f"\n[SUCCESS] File compiled successfully. Total records stored: {len(sorted_records)}")
            print(f"[INFO] Location saved: {os.path.abspath(self.export_filename)}")
        except Exception as e:
            print(f"[ERROR] Failed to compile ledger file: {e}")

# 1. Initialize exporter for your active batch session
exporter = AttendanceLedgerExporter(course_code="CSE-304G")
exporter.export_to_csv()

print("=================================================")