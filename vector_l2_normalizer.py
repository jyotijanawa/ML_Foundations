import time
import math

print("=================================================")
print("FACIAL EMBEDDING L2 VECTOR NORMALIZER ACTIVE")
print("=================================================")

class VectorL2Normalizer:
    def __init__(self, epsilon=1e-10):
        # Small epsilon value to prevent division by zero for null vectors
        self.epsilon = epsilon

    def compute_l2_norm(self, vector):
        """Calculates the Euclidean L2 norm ||v|| of a feature vector."""
        return math.sqrt(sum(x ** 2 for x in vector))

    def normalize_embedding(self, raw_embedding):
        print(f"[NORMALIZATION] Calculating L2 magnitude across {len(raw_embedding)}-dim vector...")
        time.sleep(0.4)  # Simulate vector processing pass
        
        magnitude = self.compute_l2_norm(raw_embedding)
        print(f" -> Raw Feature Vector Magnitude ||v||: {magnitude:.5f}")
        
        # L2 Normalization Formula: v / max(||v||, epsilon)
        scale_denom = max(magnitude, self.epsilon)
        unit_vector = [x / scale_denom for x in raw_embedding]
        
        # Verify unit sphere mapping (magnitude should now be exactly 1.0)
        normalized_magnitude = self.compute_l2_norm(unit_vector)
        
        print("\n--- Unit Hypersphere Mapping Telemetry ---")
        print(f" -> Raw Embedding Sample  : {[round(x, 4) for x in raw_embedding[:4]]}...")
        print(f" -> L2 Normalized Unit    : {[round(x, 4) for x in unit_vector[:4]]}...")
        print(f" -> Post-Unit Vector Norm : {normalized_magnitude:.5f}")
        print("-" * 50)
        print("[SUCCESS] Embedding mapped to unit sphere (||v|| = 1.0) for distance evaluation.")
        return unit_vector

# 1. Instantiate L2 vector normalizer
normalizer = VectorL2Normalizer()

# 2. Simulate raw 5-dimensional facial embedding vector output from deep network
raw_face_vector = [1.45, -0.88, 2.31, 0.42, -1.15]

normalizer.normalize_embedding(raw_face_vector)

print("=================================================")