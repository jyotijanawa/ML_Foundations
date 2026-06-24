import numpy as np
from nms_filter import NonMaximumSuppressionFilter

print("=================================================")
print("SPATIAL BOUNDING PREDICTION AGGREGATOR ACTIVE")
print("=================================================")

class SpatialPredictionAggregator:
    def __init__(self, confidence_cutoff=0.80):
        self.cutoff = confidence_cutoff
        self.nms = NonMaximumSuppressionFilter(iou_threshold=0.40)

    def aggregate_pipeline_detections(self, raw_boxes, raw_scores):
        print("[PROCESS] Filtering low-confidence spatial arrays...")

        # 1. Filter out raw background noise predictions below our confidence cutoff
        filtered_boxes = []
        filtered_scores = []

        for box, score in zip(raw_boxes, raw_scores):
            if score >= self.cutoff:
                filtered_boxes.append(box)
                filtered_scores.append(score)

        print(f"Pruned candidate count from {len(raw_boxes)} down to {len(filtered_boxes)}")

        # 2. Run Non-Maximum Suppression to clear out tight overlapping matrix frames
        print("[PROCESS] Executing vectorized overlap resolution step...")
        best_indices = self.nms.filter_boxes(filtered_boxes, filtered_scores)

        # 3. Compile the definitive coordinate spatial outputs
        final_selections = [filtered_boxes[idx] for idx in best_indices]
        final_scores = [filtered_scores[idx] for idx in best_indices]

        return final_selections, final_scores

# 1. Simulate an unfiltered batch of coordinate detections around a student face
# Includes raw low-confidence background artifacts (Candidate 3)
simulated_raw_boxes = [
    [50, 50, 150, 150],   # Candidate 0 (True Face Box)
    [53, 52, 151, 149],   # Candidate 1 (Overlapping Duplicate)
    [48, 51, 152, 153],   # Candidate 2 (Overlapping Duplicate)
    [200, 20, 280, 100]   # Candidate 3 (False Positive / Desk Shadow)
]

simulated_raw_scores = [0.94, 0.87, 0.81, 0.42]

print("Step 1: Ingesting Unfiltered Pipeline Tensors...")
aggregator = SpatialPredictionAggregator(confidence_cutoff=0.80)

# 2. Run the processing matrix sequence
final_boxes, final_scores = aggregator.aggregate_pipeline_detections(
    simulated_raw_boxes,
    simulated_raw_scores
)

print("-" * 50)
print("Step 2: Consolidated Optimal Target Matrix Coordinates:")

for i, (box, score) in enumerate(zip(final_boxes, final_scores)):
    print(
        f"Isolated Face Window #{i} -> Coordinates: {box} | Confidence: {score * 100:.1f}%"
    )

print("=================================================")