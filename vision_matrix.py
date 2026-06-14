import numpy as np

print("=================================================")
print(" COMPUTER VISION SPATIAL RESOLUTION MATRIX ")
print("=================================================")

simulated_camera_sensor = np.array([
    [30, 45, 180, 240],
    [35, 50, 195, 250],
    [20, 40, 170, 235],
    [40, 55, 185, 245]
], dtype=np.uint8)

print("Step 1: Raw Digital Pixel Grid Input Streams:")
print(simulated_camera_sensor)
print("-" * 50)

boosted_matrix = np.clip(simulated_camera_sensor * 1.2, 0, 255).astype(np.uint8)

print(" Step 2: Illumination & Contrast Boost Applied:")
print(boosted_matrix)
print("-" * 50)

threshold_limit = 150
binary_edge_mask = (boosted_matrix > threshold_limit).astype(int)

print(f" Step 3: Binary Feature Boundaries Found (Threshold > {threshold_limit}):")
print(binary_edge_mask)
print("\n(Notice: Your matrix perfectly isolated the sharp structural edge!)")
print("=================================================")