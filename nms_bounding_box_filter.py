import time

print("=================================================")
print("BOUNDING BOX NON-MAXIMUM SUPPRESSION ENGINE")
print("=================================================")

class NonMaximumSuppressionFilter:
    def __init__(self, iou_threshold=0.4):
        self.iou_threshold = iou_threshold

    def calculate_iou(self, box_a, box_b):
        """Calculates Intersection over Union (IoU) ratio between two bounding boxes."""
        # Box format: [x_min, y_min, x_max, y_max]
        x1 = max(box_a[0], box_b[0])
        y1 = max(box_a[1], box_b[1])
        x2 = min(box_a[2], box_b[2])
        y2 = min(box_a[3], box_b[3])

        # Compute intersection area
        intersection_width = max(0, x2 - x1)
        intersection_height = max(0, y2 - y1)
        intersection_area = intersection_width * intersection_height

        # Compute union area
        area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
        area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
        union_area = area_a + area_b - intersection_area

        if union_area == 0:
            return 0.0

        return intersection_area / union_area

    def filter_overlapping_boxes(self, detections):
        """
        Filters duplicate overlapping bounding boxes based on confidence scores.
        detections format: list of dicts [{'box': [x1, y1, x2, y2], 'score': float}]
        """
        print(f"[NMS] Evaluating {len(detections)} candidate detections...")
        time.sleep(0.4)

        # Sort detections descending by confidence score
        sorted_detections = sorted(detections, key=lambda d: d['score'], reverse=True)
        keep_list = []

        while len(sorted_detections) > 0:
            best_detection = sorted_detections.pop(0)
            keep_list.append(best_detection)
            
            remaining = []
            for candidate in sorted_detections:
                iou = self.calculate_iou(best_detection['box'], candidate['box'])
                print(f" -> IoU against score {candidate['score']:.2f}: {iou:.3f}")
                
                # Keep candidate only if overlap is below IoU suppression threshold
                if iou < self.iou_threshold:
                    remaining.append(candidate)
                else:
                    print(f" -> [SUPPRESSED] Suppressed overlapping box (Score: {candidate['score']:.2f})")
            
            sorted_detections = remaining

        print("\n--- Non-Maximum Suppression Summary ---")
        print(f" -> Input Candidates : {len(detections)}")
        print(f" -> Retained Targets : {len(keep_list)}")
        print("-" * 50)
        print("[SUCCESS] Redundant bounding box duplicates suppressed cleanly.")
        return keep_list

# 1. Instantiate the NMS filter with an IoU threshold of 0.4
nms_engine = NonMaximumSuppressionFilter(iou_threshold=0.4)

# 2. Simulate 3 raw overlapping face detection boxes over one student
raw_detections = [
    {"box": [100, 100, 200, 200], "score": 0.92},  # Primary target face box
    {"box": [105, 102, 198, 205], "score": 0.78},  # Overlapping duplicate 1
    {"box": [300, 150, 400, 250], "score": 0.88}   # Separate face box elsewhere
]

nms_engine.filter_overlapping_boxes(raw_detections)

print("=================================================")