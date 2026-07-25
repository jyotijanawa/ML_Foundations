import time
import math

print("=================================================")
print("INTRACLASS FEATURE VARIANCE EVALUATOR ACTIVE")
print("=================================================")

class IntraclassVarianceEvaluator:
    def __init__(self, variance_threshold=0.35):
        # Maximum allowed mean distance spread around the centroid vector
        self.variance_threshold = variance_threshold

    def compute_centroid(self, embeddings):
        """Computes element-wise average vector across multiple embedding samples."""
        num_samples = len(embeddings)
        vector_dim = len(embeddings[0])
        
        centroid = [
            sum(sample[dim] for sample in embeddings) / num_samples
            for dim in range(vector_dim)
        ]
        return centroid

    def calculate_euclidean_distance(self, vec_a, vec_b):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec_a, vec_b)))

    def evaluate_spread(self, student_id, embedding_samples):
        print(f"[VARIANCE_EVAL] Processing {len(embedding_samples)} sample vectors for Student ID: {student_id}...")
        time.sleep(0.4)  # Simulate matrix computation overhead
        
        centroid = self.compute_centroid(embedding_samples)
        print(f" -> Computed Centroid Vector: {[round(x, 4) for x in centroid]}")
        
        distances = [self.calculate_euclidean_distance(sample, centroid) for sample in embedding_samples]
        mean_spread = sum(distances) / len(distances)
        
        print("\n--- Intraclass Feature Dispersion Telemetry ---")
        print(f" -> Distance Spread Per Sample : {[round(d, 4) for d in distances]}")
        print(f" -> Average Intraclass Spread  : {mean_spread:.4f} (Threshold: {self.variance_threshold})")
        print("-" * 50)
        
        if mean_spread <= self.variance_threshold:
            print("[SUCCESS] Feature embeddings tightly clustered. Profile approved for master template export.")
            return True
        else:
            print("[WARNING] High intraclass variance detected! Additional enrollment samples recommended.")
            return False

# 1. Instantiate evaluator with a maximum variance threshold of 0.35
evaluator = IntraclassVarianceEvaluator(variance_threshold=0.35)

# 2. Simulate 3 enrolled 4-dimensional feature embeddings for a single student
student_samples = [
    [0.12, 0.44, -0.32, 0.85],
    [0.14, 0.41, -0.30, 0.88],
    [0.11, 0.46, -0.34, 0.83]
]

evaluator.evaluate_spread(student_id="301", embedding_samples=student_samples)

print("=================================================")