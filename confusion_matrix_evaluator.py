import time

print("=================================================")
print("FACE RECOGNITION PERFORMANCE EVALUATION ENGINE")
print("=================================================")

class ModelPerformanceEvaluator:
    def __init__(self, ground_truth_labels, predicted_labels):
        self.ground_truth = ground_truth_labels
        self.predictions = predicted_labels

    def compute_classification_metrics(self):
        print("[EVALUATION] Analyzing classification alignment across test batch...")
        time.sleep(0.4)  # Simulate batch array matrix evaluation
        
        true_positives = 0
        false_positives = 0
        false_negatives = 0
        true_negatives = 0

        for true_val, pred_val in zip(self.ground_truth, self.predictions):
            if true_val == 1 and pred_val == 1:
                true_positives += 1
            elif true_val == 0 and pred_val == 1:
                false_positives += 1
            elif true_val == 1 and pred_val == 0:
                false_negatives += 1
            elif true_val == 0 and pred_val == 0:
                true_negatives += 1

        # Prevent division by zero errors
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0.0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0.0
        f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        accuracy = (true_positives + true_negatives) / len(self.ground_truth)

        print("\n--- Diagnostic Classification Summary Matrix ---")
        print(f" -> True Positives  (TP): {true_positives}")
        print(f" -> False Positives (FP): {false_positives}")
        print(f" -> False Negatives (FN): {false_negatives}")
        print(f" -> True Negatives  (TN): {true_negatives}")
        print("-" * 50)
        print(f" -> Precision Score : {precision:.4f}")
        print(f" -> Recall Score    : {recall:.4f}")
        print(f" -> F1-Score Metric : {f1_score:.4f}")
        print(f" -> Overall Accuracy: {accuracy * 100:.2f}%")
        
        return {"precision": precision, "recall": recall, "f1": f1_score, "accuracy": accuracy}

# 1. Mock test dataset vectors (1 = Authorized Student, 0 = Unknown Intruder / Rejected)
ground_truth_batch = [1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
model_predictions  = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1] 

# 2. Instantiate and execute the evaluation suite
evaluator = ModelPerformanceEvaluator(ground_truth_batch, model_predictions)
evaluator.compute_classification_metrics()

print("=================================================")