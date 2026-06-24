import os
import json
import numpy as np

print("=================================================")
print("PERSISTENT BIOMETRIC EMBEDDING REGISTRY ACTIVE")
print("=================================================")

class EmbeddingDatabaseManager:
    def __init__(self, db_filename="biometric_registry.json"):
        self.db_path = db_filename
        self.registry = {}
        self.load_database()

    def load_database(self):
        # If database index doesn't exist, start a fresh index catalog map
        if not os.path.exists(self.db_path):
            print("[INFO] No biometric index found. Initializing blank registry scale...")
            self.registry = {}
        else:
            print("[INFO] Syncing student biometric database into local RAM index...")
            with open(self.db_path, "r", encoding="utf-8") as file:
                try:
                    self.registry = json.load(file)
                except json.JSONDecodeError:
                    self.registry = {}

    def register_student_vector(self, student_id, student_name, embedding_vector):
        # Convert NumPy array embedding list into a clear serializable Python list
        vector_list = embedding_vector.tolist() if isinstance(embedding_vector, np.ndarray) else list(embedding_vector)

        self.registry[student_id] = {
            "name": student_name,
            "vector_embedding": vector_list
        }

        # Write structural updates immediately back to disk storage
        with open(self.db_path, "w", encoding="utf-8") as file:
            json.dump(self.registry, file, indent=4)

        print(f"[REGISTERED]: Btech ID {student_id} ({student_name}) mapped successfully.")

    def get_all_registered_students(self):
        return self.registry

# 1. Initialize our localized database registry engine
db_manager = EmbeddingDatabaseManager()

print("-" * 50)
print("Simulating student biometric registration onboarding...")

# 2. Mock 4-element facial embedding vectors representing different student facial structures
mock_vector_amit = np.array([0.25, 0.88, -0.12, 0.44], dtype=np.float32)
mock_vector_priya = np.array([-0.15, 0.62, 0.45, 0.11], dtype=np.float32)

# Register profiles directly into disk cache
db_manager.register_student_vector("MDU-CSE-301", "Amit Kumar", mock_vector_amit)
db_manager.register_student_vector("MDU-CSE-305", "Priya Sharma", mock_vector_priya)

print("-" * 50)

# 3. Retrieve database tracking array
current_db = db_manager.get_all_registered_students()

print(f"Active Verified Records Count in Registry: {len(current_db)}")
print(f"Check your folder! Identity definitions written to: {db_manager.db_path}")

print("=================================================")