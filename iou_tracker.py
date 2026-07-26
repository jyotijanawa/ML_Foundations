import time

print("=================================================")
print("SPATIAL BOUNDING BOX IOU TRACKER ACTIVE")
print("=================================================")

class IoUTracker:
    def __init__(self, match_threshold=0.5):
        # Minimum IoU overlap required to consider two boxes the same face
        self.match_threshold = match_threshold

    def calculate_iou(self, box_a, box_b):
        """Computes Intersection over Union between two bounding boxes [x1, y1, x2, y2]."""
        x1 = max(box_a[0], box_b[0])
        y1 = max(box_a[1], box_b[1])
        x2 = min(box_a[2], box_b[2])
        y2 = min(box_a[3], box_b[3])

        intersection_area = max(0, x2 - x1) * max(0, y2 - y1)
        area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
        area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])
        union_area = area_a + area_b - intersection_area

        return intersection_area / union_area if union_area > 0 else 0.0

    def match_detections_to_tracks(self, active_tracks, new_detections):
        print(f"[TRACKER] Matching {len(new_detections)} new detection(s) against {len(active_tracks)} active track(s)...")
        time.sleep(0.4)

        matched_pairs = []
        unmatched_detections = list(new_detections)

        for track_id, track_box in active_tracks.items():
            best_iou = 0.0
            best_detection = None

            for det_box in unmatched_detections:
                iou = self.calculate_iou(track_box, det_box)
                print(f" -> Track '{track_id}' vs Detection {det_box}: IoU = {iou:.3f}")
                if iou > best_iou:
                    best_iou = iou
                    best_detection = det_box

            if best_iou >= self.match_threshold and best_detection:
                matched_pairs.append((track_id, best_detection))
                unmatched_detections.remove(best_detection)
                print(f" -> [MATCHED] Track '{track_id}' assigned to box {best_detection}")

        print("\n--- Association Summary Telemetry ---")
        print(f" -> Successful Matches : {len(matched_pairs)}")
        print(f" -> Unmatched Detections: {len(unmatched_detections)}")
        print("-" * 50)
        print("[SUCCESS] Bounding box tracking associations updated successfully.")
        return matched_pairs, unmatched_detections

# 1. Instantiate IoU Tracker
tracker = IoUTracker(match_threshold=0.5)

# 2. Simulate existing face track boxes from Frame N-1 and fresh detections in Frame N
existing_tracks = {
    "Track_301": [100, 100, 200, 200],
    "Track_305": [300, 150, 400, 250]
}

incoming_detections = [
    [105, 102, 202, 201],  # Slightly shifted box for Track_301
    [500, 300, 600, 400]   # Brand new face entering frame
]

tracker.match_detections_to_tracks(existing_tracks, incoming_detections)

print("=================================================")