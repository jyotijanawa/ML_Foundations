import time
import math

print("=================================================")
print("SPATIAL FACE MATRIX NORMALIZER & STANDARDIZER ACTIVE")
print("=================================================")

class FaceMatrixNormalizer:
    def __init__(self, target_scale="zscore"):
        # Normalization mode: 'minmax' [0,1] or 'zscore' (mean=0, std=1)
        self.target_scale = target_scale

    def compute_matrix_stats(self, flat_pixels):
        mean = sum(flat_pixels) / len(flat_pixels)
        variance = sum((p - mean) ** 2 for p in flat_pixels) / len(flat_pixels)
        std_dev = math.sqrt(variance)
        return mean, std_dev

    def normalize_matrix(self, image_matrix):
        print(f"[PREPROCESSING] Initiating matrix transform via mode: '{self.target_scale.upper()}'...")
        time.sleep(0.4)  # Simulate matrix transformation processing
        
        flat_pixels = [pixel for row in image_matrix for pixel in row]
        mean, std_dev = self.compute_matrix_stats(flat_pixels)
        
        print(f" -> Input Matrix Statistics: Mean = {mean:.2f} | StdDev = {std_dev:.2f}")
        time.sleep(0.3)

        normalized_matrix = []
        for row in image_matrix:
            if self.target_scale == "zscore":
                # Z-Score Formula: (x - mean) / std_dev
                norm_row = [(p - mean) / std_dev if std_dev > 0 else 0.0 for p in row]
            else:
                # Min-Max Scaling Formula: x / 255.0
                norm_row = [p / 255.0 for p in row]
            normalized_matrix.append(norm_row)

        print("\n--- Tensor Normalization Output Telemetry ---")
        print(f" -> Raw RGB Pixel Row (0-255) : {image_matrix[0]}")
        print(f" -> Normalized Float Row      : {[round(x, 4) for x in normalized_matrix[0]]}")
        print("-" * 50)
        print("[SUCCESS] Matrix tensor scaling complete. Ready for neural network input layer.")
        return normalized_matrix

# 1. Instantiate the face matrix normalizer with Z-score mode
normalizer = FaceMatrixNormalizer(target_scale="zscore")

# 2. Simulate a raw 4x4 grayscale cropped face matrix (intensity values 0-255)
raw_face_matrix = [
    [120, 135, 150, 162],
    [118, 128, 142, 158],
    [90,  105, 115, 130],
    [85,  98,  110, 125]
]

normalizer.normalize_matrix(raw_face_matrix)

print("=================================================")