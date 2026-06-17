import numpy as np

print("=================================================")
print("ADAPTIVE SPATIAL HISTOGRAM EQUALIZER ACTIVE")
print("=================================================")

class HistogramEqualizer:
    def __init__(self):
        pass

    def equalize_image_matrix(self, low_contrast_matrix):
        flat_pixels = low_contrast_matrix.flatten()

        pixel_counts = np.bincount(flat_pixels, minlength=256)

        cumulative_sum = np.cumsum(pixel_counts)

        cdf_masked = np.ma.masked_equal(cumulative_sum, 0)
        cdf_normalized = ((cdf_masked - cdf_masked.min()) * 255) / (cdf_masked.max() - cdf_masked.min())
        cdf_final = np.ma.filled(cdf_normalized, 0).astype(np.uint8)

        equalized_matrix = cdf_final[low_contrast_matrix]
        return equalized_matrix

underexposed_face_patch = np.array([
    [10, 12, 15, 11],
    [12, 25, 22, 14],
    [11, 20, 18, 12],
    [10, 14, 15, 13]
], dtype=np.uint8)

print("Step 1: Raw Underexposed Face Pixel Patch:")
print(underexposed_face_patch)
print("-" * 50)

equalizer = HistogramEqualizer()
balanced_face_patch = equalizer.equalize_image_matrix(underexposed_face_patch)

print("Step 2: Adaptive Histogram Equalization Matrix Output:")
print(balanced_face_patch)
print("\nThe narrow dark contrast band has been stretched from 0 to 255.")
print("=================================================")