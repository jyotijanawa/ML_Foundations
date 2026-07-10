import time

print("=================================================")
print("STUDENT ENROLLMENT RECORD STRUCTURER ACTIVE")
print("=================================================")

class EnrollmentRecordStructurer:
    def __init__(self):
        # Target academic parameters
        self.default_department = "CSE"
        self.default_year = 3

    def structure_profile(self, raw_name, roll_no, current_batch="Core-A"):
        print(f"[PROCESS] Formatting enrollment schema for Roll No: {roll_no}...")
        time.sleep(0.4)  # Simulate object allocation delay
        
        # Packing loose parameters into a clean, uniform data dictionary structure
        structured_profile = {
            "identity_meta": {
                "full_name": raw_name,
                "roll_number": roll_no
            },
            "academic_meta": {
                "department_code": self.default_department,
                "academic_year_level": self.default_year,
                "assigned_batch_group": current_batch
            },
            "system_meta": {
                "profile_initialized": True,
                "timestamp_logged": time.strftime("%Y-%m-%d")
            }
        }
        
        print("\n--- Standardized Profile Data Model Structure ---")
        print(f" -> Name      : {structured_profile['identity_meta']['full_name']}")
        print(f" -> Dept/Year : B.Tech {structured_profile['academic_meta']['department_code']} (Year {structured_profile['academic_meta']['academic_year_level']})")
        print(f" -> Registry  : Status Operational | Group: {structured_profile['academic_meta']['assigned_batch_group']}")
        print("-" * 50)
        
        return structured_profile

# 1. Initialize the dataset structuring manager
structurer = EnrollmentRecordStructurer()

# 2. Simulate compiling structural record entries for the active roster
print("--- Execution Run: Compiling Student Profile Ledger ---")
structurer.structure_profile("Jyoti Sharma", "305")

print("=================================================")