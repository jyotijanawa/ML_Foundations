import time
import math

print("=================================================")
print("LOCAL FACE EMBEDDING DISTANCE MATCHER ACTIVE")
print("=================================================")

class FaceEmbeddingMatcher:
    def __init__(self, tolerance_threshold=0.6):
        # A distance below this threshold represents a positive identity match
        self.tolerance_threshold = tolerance_threshold
        
        # Mock database containing known student names and their stored 4-dimensional embeddings
        self.known_database = {
            "Jyoti Sharma": [0.15, -0.23, 0.45, 0.08],
            "Amit Kumar": [-0.05, 0.38, -0.12, 0.51]
        }

    def calculate_euclidean_distance(self, vector_a, vector_b):
        # Calculate the straight-line mathematical distance between two coordinate sets
        sum_of_squares = sum((a - b) ** 2 for a, b in zip(vector_a, vector_b))
        return math.sqrt(sum_of_squares)

    def search_identity(self, live_embedding):
        print("[MATCHING] Computing spatial vector distances against database records...")
        time.sleep(0.4)  # Simulate system execution latency
        
        best_match_name = "Unknown"
        lowest_distance = float('inf')

        for student_name, stored_embedding in self.known_database.items():
            distance = self.calculate_euclidean_distance(live_embedding, stored_embedding)
            print(f" -> Distance to {student_name}: {distance:.4f}")
            
            if distance < lowest_distance:
                lowest_distance = distance
                if distance <= self.tolerance_threshold:
                    best_match_name = student_name

        print("-" * 50)
        if best_match_name != "Unknown":
            print(f"[SUCCESS] Face Identified: {best_match_name} (Distance: {lowest_distance:.4f})")
        else:
            print(f"[UNKNOWN] Identity verification failed. Closest distance ({lowest_distance:.4f}) exceeds safety threshold.")
        
        return best_match_name

# 1. Initialize the vector comparison engine
matcher = FaceEmbeddingMatcher(tolerance_threshold=0.6)

# 2. Simulate capturing a live face embedding (close match to Jyoti's stored vector)
live_captured_face = [0.18, -0.21, 0.42, 0.11] 

print("--- Live Scan Verification Stage ---")
matcher.search_identity(live_captured_face)

print("=================================================")