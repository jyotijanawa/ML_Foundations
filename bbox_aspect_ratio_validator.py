import time

print("=================================================")
print("SPATIAL BBOX ASPECT RATIO VALIDATOR ACTIVE")
print("=================================================")

class BoundingBoxAspectRatioValidator:
    def __init__(self, min_ratio=0.65, max_ratio=1.35, min_area=1600):
        # Aspect ratio range (width / height) typical for frontal/near-frontal face crops
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio
        # Minimum pixel area threshold (e.g., 40x40 pixels) to reject tiny distant faces
        self.min_area = min_area

    def validate_box_geometry(self, box_id, bbox_coords):
        """
        Validates bounding box dimensions.
        bbox_coords format: [x_min, y_min, x_max, y_max]
        """
        x_min, y_min, x_max, y_max = bbox_coords
        width = x_max - x_min
        height = y_max - y_min

        print(f"[VALIDATOR] Evaluating '{box_id}' geometry: Dim ({width}x{height} px)...")
        time.sleep(0.4)  # Simulate spatial metric calculation

        if height <= 0 or width <= 0:
            print(" -> [REJECTED] Invalid box dimensions (zero or negative area).")
            return False

        area = width * height
        aspect_ratio = width / float(height)

        print("\n--- Geometric Ratio Telemetry ---")
        print(f" -> Bounding Box Area : {area} px^2 (Min Required: {self.min_area})")
        print(f" -> Computed Ratio    : {aspect_ratio:.3f} (Valid Band: [{self.min_ratio} - {self.max_ratio}])")
        print("-" * 50)

        if area < self.min_area:
            print(f" -> [REJECTED] Crop area too small ({area} < {self.min_area}). Face too far from camera.")
            return False

        if self.min_ratio <= aspect_ratio <= self.max_ratio:
            print("[SUCCESS] Bounding box aspect ratio verified. Crop approved for neural network.")
            return True
        else:
            print(f" -> [REJECTED] Aspect ratio anomaly ({aspect_ratio:.2f}). Profile stretched or side-facing.")
            return False

# 1. Instantiate validator with default facial geometry limits
validator = BoundingBoxAspectRatioValidator(min_ratio=0.65, max_ratio=1.35, min_area=1600)

# 2. Simulate 3 distinct bounding box detections from video frame
test_boxes = {
    "Target_Face_Valid": [120, 80, 220, 200],    # Width=100, Height=120 -> Ratio ~0.83, Area=12000 (VALID)
    "Distorted_Poster": [50, 40, 250, 80],      # Width=200, Height=40  -> Ratio = 5.0 (REJECTED)
    "Distant_Noise": [300, 300, 320, 320]        # Width=20, Height=20   -> Area = 400 (REJECTED)
}

for b_id, coords in test_boxes.items():
    validator.validate_box_geometry(b_id, coords)
    print()

print("=================================================")