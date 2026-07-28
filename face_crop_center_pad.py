import time

print("=================================================")
print("DYNAMIC FACE CROP CENTERING ENGINE ACTIVE")
print("=================================================")

class FaceCropCenterPadEngine:
    def __init__(self, padding_factor=0.20):
        # 20% margin expansion around face bounding box
        self.padding_factor = padding_factor

    def compute_padded_crop_coordinates(self, bbox, frame_shape):
        """
        Expands and centers bounding box coordinates safely within frame limits.
        bbox format: [x_min, y_min, x_max, y_max]
        frame_shape format: (height, width)
        """
        x_min, y_min, x_max, y_max = bbox
        frame_h, frame_w = frame_shape

        width = x_max - x_min
        height = y_max - y_min

        print(f"[CROP_ENGINE] Input Box: [{x_min}, {y_min}, {x_max}, {y_max}] (Dimensions: {width}x{height} px)")
        time.sleep(0.4)  # Simulate spatial coordinate calculation

        # Calculate box centroid
        center_x = x_min + (width / 2.0)
        center_y = y_min + (height / 2.0)

        # Apply padding expansion based on largest dimension to form a square box
        max_dim = max(width, height)
        padded_dim = max_dim * (1.0 + self.padding_factor)
        half_dim = padded_dim / 2.0

        # Calculate new padded bounding box
        new_x_min = int(center_x - half_dim)
        new_y_min = int(center_y - half_dim)
        new_x_max = int(center_x + half_dim)
        new_y_max = int(center_y + half_dim)

        # Safe boundary clipping against camera resolution limits
        safe_x_min = max(0, new_x_min)
        safe_y_min = max(0, new_y_min)
        safe_x_max = min(frame_w, new_x_max)
        safe_y_max = min(frame_h, new_y_max)

        print("\n--- Spatial Centering & Boundary Padding Telemetry ---")
        print(f" -> Centroid Point (Cx, Cy) : ({center_x:.1f}, {center_y:.1f})")
        print(f" -> Expanded Square Dim    : {int(padded_dim)}x{int(padded_dim)} px")
        print(f" -> Safe Clipped Coordinates: [{safe_x_min}, {safe_y_min}, {safe_x_max}, {safe_y_max}]")
        print("-" * 50)
        print("[SUCCESS] Face crop centered and padded safely within frame bounds.")

        return [safe_x_min, safe_y_min, safe_x_max, safe_y_max]

# 1. Instantiate the crop centering engine with 20% margin expansion
crop_engine = FaceCropCenterPadEngine(padding_factor=0.20)

# 2. Simulate a face bounding box near the top-left boundary of a 1080p camera feed
camera_resolution = (1080, 1920)  # (Height, Width)
tight_face_box = [15, 10, 115, 130]  # x_min=15, y_min=10 (close to frame boundary)

crop_engine.compute_padded_crop_coordinates(tight_face_box, camera_resolution)

print("=================================================")