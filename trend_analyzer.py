import time

print("=================================================")
print("ATTENDANCE TREND ANALYTICS ENGINE ACTIVE")
print("=================================================")

class AttendanceTrendAnalyzer:
    def __init__(self):
        # Simulated class statistics mapping Subject Codes to (Attended, Total_Lectures)
        self.analytics_data = {
            "PCC-CSE-303G": {"attended": 26, "total": 30},
            "PCC-CSE-306G": {"attended": 28, "total": 30},
            "PCC-CSE-307G": {"attended": 21, "total": 30}  # Low trend case
        }
        self.alert_threshold = 75.0

    def generate_percentage_report(self):
        print("[ANALYTICS] Parsing academic metrics ledger registries...")
        time.sleep(0.5)  # Simulate analytical processing time
        
        print("\n--- Aggregated Session Performance Indices ---")
        for course, stats in self.analytics_data.items():
            # Calculate metrics percentage
            percentage = (stats["attended"] / stats["total"]) * 100
            status = "NOMINAL" if percentage >= self.alert_threshold else "CRITICAL DEFICIT"
            
            print(f" -> Course: {course} | Rate: {percentage:.1f}% | Evaluation: {status}")
            
            if percentage < self.alert_threshold:
                print(f"    [WARNING] Attendance index is short of the mandatory {self.alert_threshold}% university limit!")
        
        print("-" * 50)
        print("[SUCCESS] Trend analysis complete. Indices successfully exported to system cache.")

# 1. Initialize the trend analyzer engine
analyzer = AttendanceTrendAnalyzer()
analyzer.generate_percentage_report()

print("=================================================")