import time

print("=================================================")
print("STUDENT ENROLLMENT REGISTRY MODULE ACTIVE")
print("=================================================")

class StudentRegistry:
    def __init__(self):
        # Local structural database storage simulation
        # Maps Roll Number -> Student Name and Profile Verification Status
        self.enrolled_students = {
            "301": {"name": "Amit Kumar", "face_vector_cached": True},
            "305": {"name": "Priya Sharma", "face_vector_cached": True},
            "312": {"name": "Rahul Verma", "face_vector_cached": True}
        }

    def register_new_student(self, roll_no, name):
        print(f"\n[REGISTRATION] Attempting enrollment for Roll No: {roll_no} ({name})...")
        time.sleep(0.4) # Simulate processing check delay
        
        # Check if student is already in the database
        if roll_no in self.enrolled_students:
            print(f"[REJECTED] Conflict detected! Roll No {roll_no} is already registered to '{self.enrolled_students[roll_no]['name']}'.")
            return False
            
        # Securely save the new record and flag face data validation
        self.enrolled_students[roll_no] = {"name": name, "face_vector_cached": True}
        print(f"[SUCCESS] Student profile created. Face vector arrays mapped to database records.")
        return True

    def display_active_roster(self):
        print(f"\n--- Total Enrolled Roster Size: {len(self.enrolled_students)} Students ---")
        for roll_no, data in sorted(self.enrolled_students.items()):
            print(f" Roll No: {roll_no.ljust(5)} | Name: {data['name'].ljust(15)} | Vector Status: VALID")

# 1. Initialize the system registry manager
registry = StudentRegistry()

# 2. Display starting student database state
registry.display_active_roster()
print("-" * 50)

# 3. Simulate adding a brand new student
registry.register_new_student("320", "Sneha Gupta")

# 4. Simulate a duplicate collision check
registry.register_new_student("305", "Duplicate Check Entry")
print("-" * 50)

# 5. Display finalized database status
registry.display_active_roster()

print("=================================================")