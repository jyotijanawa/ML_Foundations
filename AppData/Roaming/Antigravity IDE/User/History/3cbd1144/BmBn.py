import os
import numpy as np

print("=================================================")
print("VISION MATRIX DOWNSAMPLER & BINARY POOLER")
print("=================================================")

class ImageMatrixPooler:
    def __init__(self, cache_dir="./face_cache"):
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
            print(f"[INFO] Created binary pool directory: {self.cache_dir}")

    def downsample_block_average(self, matrix):
        return (
            matrix[0::2, 0::2] // 4 +
            matrix[1::2, 0::2] // 4 +
            matrix[0::2, 1::2] // 4 +
            matrix[1::2, 1::2] // 4
        )

    def serialize_to_pool(self, filename, matrix):
        filepath = os.path.join(self.cache_dir, filename)
        np.save(filepath, matrix)
        print(f"[SUCCESS] Compressed feature matrix pool saved to: {filepath}.npy")

high_res_face_crop = np.array([
    [200, 204, 80, 88],
    [196, 200, 76, 84],
    [120, 124, 240, 244],
    [116, 120, 236, 240]
], dtype=np.uint8)

print("Step 1: High-Resolution Face Crop Matrix (4x4):")
print(high_res_face_crop)
print("-" * 50)

pooler = ImageMatrixPooler()

compressed_matrix = pooler.downsample_block_average(high_res_face_crop)

print("Step 2: Downsampled Structural Representation Matrix (2x2):")
print(compressed_matrix)
print("-" * 50)

pooler.serialize_to_pool("student_01_feature", compressed_matrix)

print("=================================================")