import numpy as np

print("=================================================")
print("NON-MAXIMUM SUPPRESSION MATRIX FILTER ACTIVE")
print("=================================================")

class NonMaximumSuppressionFilter:
    def __init__(self, iou_threshold=0.40):
        self.iou_thresh = iou_threshold

    def filter_boxes(self, boxes, scores):
        if len(boxes) == 0:
            return []

        boxes = np.array(boxes, dtype=np.float32)
        scores = np.array(scores, dtype=np.float32)

        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]

        areas = (x2 - x1) * (y2 - y1)

        order = scores.argsort()[::-1]
        keep_indices = []

        while order.size > 0:
            best_box_idx = order[0]
            keep_indices.append(best_box_idx)

            if order.size == 1:
                break

            xx1 = np.maximum(x1[best_box_idx], x1[order[1:]])
            yy1 = np.maximum(y1[best_box_idx], y1[order[1:]])
            xx2 = np.minimum(x2[best_box_idx], x2[order[1:]])
            yy2 = np.minimum(y2[best_box_idx], y2[order[1:]])

            w = np.maximum(0.0, xx2 - xx1)
            h = np.maximum(0.0, yy2 - yy1)
            intersection = w * h

            iou = intersection / (
                areas[best_box_idx] +
                areas[order[1:]] -
                intersection
            )

            under_threshold_indices = np.where(
                iou <= self.iou_thresh
            )[0]

            order = order[under_threshold_indices + 1]

        return keep_indices

mock_boxes = [
    [50, 50, 150, 150],
    [52, 54, 152, 154],
    [55, 48, 158, 148]
]

mock_scores = [0.96, 0.88, 0.74]

print("Step 1: Raw Unfiltered Overlapping Detections Queue:")
for i, (b, s) in enumerate(zip(mock_boxes, mock_scores)):
    print(f"Box #{i} : Coordinates {b} | Confidence: {s * 100:.1f}%")

print("-" * 50)

nms_engine = NonMaximumSuppressionFilter(iou_threshold=0.40)
optimized_indices = nms_engine.filter_boxes(
    mock_boxes,
    mock_scores
)

print("Step 2: Non-Maximum Suppression Active Selection:")
print(f"Optimized Saved Bounding Box Index: {optimized_indices}")

print("\n(Notice: Duplicate bounding boxes were cleanly suppressed from layout!)")
print("=================================================")