import time
import math

print("=================================================")
print("FACIAL LANDMARK AFFINE MATRIX ROTATOR ACTIVE")
print("=================================================")

class AffineMatrixRotator:
    def __init__(self, output_shape=(112, 112)):
        # Output spatial canvas size (Width, Height) for network input
        self.output_shape = output_shape

    def compute_affine_matrix(self, center, angle_degrees, scale):
        """Constructs a 2x3 Affine Transformation Matrix for rotation and scaling."""
        angle_rad = math.radians(angle_degrees)
        alpha = scale * math.cos(angle_rad)
        beta = scale * math.sin(angle_rad)

        cx, cy = center
        # Compute translation offset to keep image centered in target canvas
        tx = (1.0 - alpha) * cx - beta * cy
        ty = beta * cx + (1.0 - alpha) * cy

        # 2x3 Transformation Matrix M = [[alpha, beta, tx], [-beta, alpha, ty]]
        matrix_m = [
            [alpha, beta, tx],
            [-beta, alpha, ty]
        ]
        return matrix_m

    def transform_point(self, point, matrix_m):
        """Maps a 2D coordinate (x, y) through the 2x3 affine matrix M."""
        x, y = point
        x_prime = matrix_m[0][0] * x + matrix_m[0][1] * y + matrix_m[0][2]
        y_prime = matrix_m[1][0] * x + matrix_m[1][1] * y + matrix_m[1][2]
        return (x_prime, y_prime)

    def process_rotation_pass(self, center_point, angle, scale, landmark_point):
        print(f"[TRANSFORM] Constructing 2x3 Affine Matrix (Angle: {angle:.1f}°, Scale: {scale:.2f}x)...")
        time.sleep(0.4)  # Simulate matrix construction overhead

        matrix_m = self.compute_affine_matrix(center_point, angle, scale)
        transformed_landmark = self.transform_point(landmark_point, matrix_m)

        print("\n--- Affine Transformation Matrix Telemetry ---")
        print(f" -> Matrix Row 0 [alpha, beta, tx] : {[round(v, 4) for v in matrix_m[0]]}")
        print(f" -> Matrix Row 1 [-beta, alpha, ty]: {[round(v, 4) for v in matrix_m[1]]}")
        print(f" -> Original Landmark Coord        : {landmark_point}")
        print(f" -> Aligned Target Landmark Coord  : ({transformed_landmark[0]:.2f}, {transformed_landmark[1]:.2f})")
        print("-" * 50)
        print("[SUCCESS] Spatial grid mapped smoothly across 2D affine transformation.")
        return matrix_m

# 1. Instantiate the affine rotator
rotator = AffineMatrixRotator(output_shape=(112, 112))

# 2. Simulate rotating a face tilted 12 degrees clockwise around center (56, 56)
face_center = (56, 56)
tilt_angle = 12.0
scale_factor = 1.05
sample_eye_landmark = (42, 48)

rotator.process_rotation_pass(face_center, tilt_angle, scale_factor, sample_eye_landmark)

print("=================================================")