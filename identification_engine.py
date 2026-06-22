import numpy as np

# 1. Importing database registry concept safely
from embedding_db import EmbeddingDatabaseManager

print("=================================================")
print("BIOMETRIC REAL-TIME IDENTIFICATION ENGINE ACTIVE")
print("=================================================")

# 2. Matcher class contained directly inside this file
class FaceEmbeddingMatcher:
    def __init__(self, match_threshold=0.20):
        self.threshold = match_threshold

    def compute_euclidean_distance(self, embedding_a, embedding_b):
        return np.sqrt(np.sum(np.square(embedding_a - embedding_b)))

class IdentityVerificationEngine:
    def __init__(self, verification_threshold=0.20):
        self.db = EmbeddingDatabaseManager()
        self.matcher = FaceEmbeddingMatcher(match_threshold=verification_threshold)

    def identify_face_vector(self, live_scan_vector):
        print("\n[SCAN RECEIVED] Running multi-profile database matrix match...")
        registered_records = self.db.get_all_registered_students()
        
        best_match_id = None
        best_match_name = None
        lowest_distance = float('inf')

        # Iterate through every student record registered inside our JSON disk cache
        for student_id, profile in registered_records.items():
            db_vector = np.array(profile["vector_embedding"], dtype=np.float32)
            
            # Compute exact spatial Euclidean distance
            distance = self.matcher.compute_euclidean_distance(live_scan_vector, db_vector)
            
            if distance < lowest_distance:
                lowest_distance = distance
                best_match_id = student_id
                best_match_name = profile["name"]

        # Apply safety threshold check
        if lowest_distance <= self.matcher.threshold:
            print(f"Identity Found! Match Confidence Margin Distance: {lowest_distance:.4f}")
            return best_match_id, best_match_name
        else:
            print(f"Identity Unknown. Closest match margin ({lowest_distance:.4f}) exceeded safety threshold constraint.")
            return None, "Unknown Intruder"

# Initialize our unified identification supervisor environment
id_system = IdentityVerificationEngine(verification_threshold=0.18)

# Simulate a live facial capture query (matching Amit Kumar's profile)
mock_incoming_face_vector = np.array([0.26, 0.86, -0.11, 0.45], dtype=np.float32)

# Execute lookup
matched_id, matched_name = id_system.identify_face_vector(mock_incoming_face_vector)

print("-" * 50)
print("Processing Identification Results Dashboard:")
print(f"Resolution Status : {matched_name} | ID Registration Reference: {matched_id}")
print("=================================================")