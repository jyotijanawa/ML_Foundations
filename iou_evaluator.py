import numpy as np

print("=================================================")
print("SPATIAL OVERLAP IoU METRIC ENGINE ACTIVE")
print("=================================================")

class BoundingBoxIoUEvaluator:
    def __init__(self):
        pass

    def compute_iou(self, box_a, box_b):
        x_min_inter = max(box_a[0], box_b[0])
        y_min_inter = max(box_a[1], box_b[1])
        x_max_inter = min(box_a[2], box_b[2])
        y_max_inter = min(box_a[3], box_b[3])

        inter_width = max(0, x_max_inter - x_min_inter)
        inter_height = max(0, y_max_inter - y_min_inter)
        intersection_area = inter_width * inter_height

        area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
        area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

        union_area = float(area_a + area_b - intersection_area)
        if union_area == 0:
            return 0.0

        return intersection_area / union_area

ground_truth_box = np.array([50, 50, 150, 150])
current_detect_box = np.array([60, 60, 160, 160])

print("Step 1: Simulated Bounding Box Coordinates:")
print(f"Box A (Ground Truth)   : {ground_truth_box}")
print(f"Box B (Live Detection) : {current_detect_box}")
print("-" * 50)

evaluator = BoundingBoxIoUEvaluator()
iou_score = evaluator.compute_iou(ground_truth_box, current_detect_box)

print("Step 2: Spatial Overlap Evaluation Analysis:")
print(f"Calculated Overlap Metric : {iou_score * 100:.2f}% IoU")

threshold = 0.50
if iou_score >= threshold:
    print(f"\n[MATCH CONFIRMED]: IoU is above threshold ({threshold * 100}%). These belong to the same student face!")
else:
    print(f"\n[DISTINCT FEATURES]: Distinct objects or separate students tracked.")

print("=================================================")