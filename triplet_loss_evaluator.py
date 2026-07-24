import time
import math

print("=================================================")
print("TRIPLET LOSS EMBEDDING METRIC EVALUATOR ACTIVE")
print("=================================================")

class TripletLossEvaluator:
    def __init__(self, margin=0.2):
        # Alpha margin parameter enforcing embedding cluster separation
        self.margin = margin

    def compute_squared_euclidean_distance(self, vec_a, vec_b):
        """Calculates L2 squared distance between two high-dimensional feature vectors."""
        return sum((a - b) ** 2 for a, b in zip(vec_a, vec_b))

    def evaluate_triplet_loss(self, anchor_vec, positive_vec, negative_vec):
        print(f"[LOSS_EVAL] Calculating spatial embedding distances (Margin Alpha = {self.margin})...")
        time.sleep(0.4)  # Simulate vector metric processing
        
        d_pos = self.compute_squared_euclidean_distance(anchor_vec, positive_vec)
        d_neg = self.compute_squared_euclidean_distance(anchor_vec, negative_vec)
        
        print(f" -> Anchor-Positive Squared Distance (d_pos): {d_pos:.4f}")
        print(f" -> Anchor-Negative Squared Distance (d_neg): {d_neg:.4f}")
        
        # Triplet Loss Formula: max(0, d_pos - d_neg + margin)
        loss = max(0.0, d_pos - d_neg + self.margin)
        
        print("\n--- Feature Space Optimization Telemetry ---")
        print(f" -> Distance Difference (d_pos - d_neg) : {d_pos - d_neg:.4f}")
        print(f" -> Computed Triplet Loss               : {loss:.4f}")
        print("-" * 50)
        
        if loss == 0.0:
            print("[SUCCESS] Satisfies margin constraint. No gradient penalty required.")
        else:
            print("[WARNING] Semi-hard or hard triplet detected. Backpropagation gradient active.")
            
        return loss

# 1. Instantiate evaluator with a margin threshold of 0.2
evaluator = TripletLossEvaluator(margin=0.2)

# 2. Simulate 4-dimensional normalized feature embeddings
# Anchor & Positive are close in space; Negative is distant
anchor_embedding   = [0.12, 0.45, -0.33, 0.88]
positive_embedding = [0.15, 0.42, -0.30, 0.85]
negative_embedding = [-0.40, 0.10, 0.65, 0.12]

evaluator.evaluate_triplet_loss(anchor_embedding, positive_embedding, negative_embedding)

print("=================================================")