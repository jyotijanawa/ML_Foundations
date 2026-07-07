import time

print("=================================================")
print("ROLL NUMBER TO BIOMETRIC PROFILE MAPPER ACTIVE")
print("=================================================")

class RollBiometricMapper:
    def __init__(self):
        # Local look-up matrix mapping Vector ID -> Official University Roll Number
        self.biometric_registry = {
            "vec_001": "301",
            "vec_002": "305",
            "vec_003": "312",
            "vec_004": "320"
        }

    def find_roll_by_vector(self, vector_id):
        print(f"[LOOKUP] Searching biometric directory for profile pointer: {vector_id}...")
        time.sleep(0.4)  # Simulate dictionary key lookup extraction delay
        
        if vector_id in self.biometric_registry:
            associated_roll = self.biometric_registry[vector_id]
            print(f"[MATCH FOUND] Vector index {vector_id} securely maps to Roll No: {associated_roll}")
            return associated_roll
        else:
            print(f"[UNKNOWN PROFILE] Warning: Vector pointer {vector_id} does not match any registered student.")
            return None

# 1. Initialize the identity mapping node
mapper = RollBiometricMapper()

# 2. Simulate a successful classroom face detection look-up
print("--- Scenario A: Validating Recognized Face Array ---")
mapper.find_roll_by_vector("vec_002")

print("-" * 55)

# 3. Simulate an unrecognized guest or unknown profile flag
print("--- Scenario B: Validating Unregistered Face Array ---")
mapper.find_roll_by_vector("vec_999")

print("=================================================")