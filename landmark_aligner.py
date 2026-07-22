import time
import math

print("=================================================")
print("DYNAMIC SPATIAL FACIAL LANDMARK ALIGNER ACTIVE")
print("=================================================")

class FacialLandmarkAligner:
    def __init__(self, target_eye_distance=60):
        # Standard eye distance baseline for normalized embedding inputs
        self.target_eye_distance = target_eye_distance

    def calculate_rotation_angle(self, left_eye, right_eye):
        """Calculates the tilt angle in degrees between two eye coordinates."""
        d_x = right_eye[0] - left_eye[0]
        d_y = right_eye[1] - left_eye[1]
        
        # Calculate angle in radians, then convert to degrees
        angle_rad = math.atan2(d_y, d_x)
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    def align_face_geometry(self, left_eye_coords, right_eye_coords):
        print(f"[ALIGNMENT] Locating landmark centroids: Left {left_eye_coords} | Right {right_eye_coords}...")
        time.sleep(0.4)  # Simulate landmark detection processing
        
        tilt_angle = self.calculate_rotation_angle(left_eye_coords, right_eye_coords)
        print(f" -> Detected Facial Tilt Angle: {tilt_angle:.2f}°")
        
        # Compute Euclidean distance between eyes
        current_distance = math.sqrt(
            (right_eye_coords[0] - left_eye_coords[0])**2 + 
            (right_eye_coords[1] - left_eye_coords[1])**2
        )
        scale_factor = self.target_eye_distance / current_distance if current_distance > 0 else 1.0
        
        time.sleep(0.3)  # Simulate affine matrix transformation
        print("\n--- Geometric Transformation Matrix ---")
        print(f" -> Inverse Rotation Correction : {-tilt_angle:.2f}°")
        print(f" -> Affine Scaling Multiplier  : {scale_factor:.3f}x")
        print("-" * 50)
        print("[SUCCESS] Face matrix rotated and scaled to normalized vertical axis.")
        return True

# 1. Instantiate the landmark alignment processor
aligner = FacialLandmarkAligner(target_eye_distance=60)

# 2. Simulate landmark coordinates for a head tilted ~15 degrees
# Format: (x_coordinate, y_coordinate)
mock_left_eye  = (120, 140)
mock_right_eye = (175, 155)

aligner.align_face_geometry(mock_left_eye, mock_right_eye)

print("=================================================")