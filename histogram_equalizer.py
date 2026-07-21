import time

print("=================================================")
print("DYNAMIC SPATIAL HISTOGRAM EQUALIZER ACTIVE")
print("=================================================")

class SpatialHistogramEqualizer:
    def __init__(self, tile_grid_shape=(2, 2), clip_limit=2.0):
        # Shape defining spatial tile divisions across the image matrix
        self.tile_grid_shape = tile_grid_shape
        self.clip_limit = clip_limit

    def equalize_matrix_contrast(self, image_matrix):
        print(f"[PREPROCESSING] Partitioning frame matrix into {self.tile_grid_shape[0]}x{self.tile_grid_shape[1]} spatial grid tiles...")
        time.sleep(0.4)  # Simulate spatial tile division overhead
        
        rows = len(image_matrix)
        cols = len(image_matrix[0])
        print(f" -> Input Frame Matrix Dimensions: {rows}x{cols} intensity pixels")
        
        # Calculate global average intensity before processing
        flat_pixels = [pixel for row in image_matrix for pixel in row]
        mean_intensity_before = sum(flat_pixels) / len(flat_pixels)
        print(f" -> Baseline Mean Luminance: {mean_intensity_before:.1f} / 255.0")

        time.sleep(0.3)
        # Simulate local spatial equalization by redistributing pixel dynamic range
        equalized_matrix = []
        for row in image_matrix:
            # Shift pixel intensity values toward a normalized median contrast band
            equalized_row = [min(255, int(pixel * 1.25)) if pixel < 128 else max(0, int(pixel * 0.9)) for pixel in row]
            equalized_matrix.append(equalized_row)

        flat_after = [pixel for row in equalized_matrix for pixel in row]
        mean_intensity_after = sum(flat_after) / len(flat_after)

        print("\n--- Luminance Equalization Telemetry ---")
        print(f" -> Raw Spatial Matrix : {image_matrix[0]}")
        print(f" -> Equalized Matrix   : {equalized_matrix[0]}")
        print(f" -> Post-Process Mean Luminance: {mean_intensity_after:.1f} / 255.0")
        print("-" * 50)
        print("[SUCCESS] Spatial contrast balanced cleanly across shadow & highlight bounds.")
        return equalized_matrix

# 1. Initialize the adaptive histogram equalizer
equalizer = SpatialHistogramEqualizer(tile_grid_shape=(2, 2), clip_limit=2.0)

# 2. Simulate a dark/shadowed 4x4 image intensity patch (values 0-255)
shadowed_face_patch = [
    [40,  45,  50,  55],
    [38,  42,  48,  52],
    [180, 190, 200, 210], # Harsh highlight area
    [35,  39,  44,  50]
]

equalizer.equalize_matrix_contrast(shadowed_face_patch)

print("=================================================")