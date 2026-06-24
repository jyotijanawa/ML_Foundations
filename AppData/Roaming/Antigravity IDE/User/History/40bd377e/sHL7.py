import numpy as np

print("=================================================")
print("VISION IMAGE MATRIX PREPROCESSOR ACTIVE")
print("=================================================")

class ImagePreprocessor:
    def __init__(self):
        pass

    def scale_to_range(self, matrix):
        return matrix.astype(np.float32) / 255.0

    def standardize_matrix(self, matrix):
        float_matrix = matrix.astype(np.float32)
        mean = np.mean(float_matrix)
        std = np.std(float_matrix)

        if std == 0:
            return float_matrix - mean

        return (float_matrix - mean) / std

face_feature_patch = np.array([
    [150, 200, 255],
    [100, 120, 180],
    [50, 80, 95]
], dtype=np.uint8)

print("Step 1: Raw Equalized Input Matrix:")
print(face_feature_patch)
print("-" * 50)

preprocessor = ImagePreprocessor()

scaled_output = preprocessor.scale_to_range(face_feature_patch)
print("Step 2: Scaled Floating-Point Matrix [0.0 - 1.0 Range]:")
print(np.round(scaled_output, 4))
print("-" * 50)

standardized_output = preprocessor.standardize_matrix(face_feature_patch)
print("Step 3: Standard Normal Distribution Matrix (Z-Score Centered):")
print(np.round(standardized_output, 4))
print(f"\nVerification -> Calculated Mean: {np.mean(standardized_output):.1f} | Standard Dev: {np.std(standardized_output):.1f}")
print("=================================================")