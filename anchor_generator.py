import numpy as np

print("=================================================")
print("EMBEDDED FEATURE SPATIAL ANCHOR ENGINE ACTIVE")
print("=================================================")

class FeatureAnchorGenerator:
    def __init__(self, base_scale=16):
        self.base_scale = base_scale

    def generate_spatial_anchors(self, grid_centers_x, grid_centers_y):
        # Using NumPy broadcasting to map anchor dimensions across coordinate arrays
        x_mesh, y_mesh = np.meshgrid(grid_centers_x, grid_centers_y)

        # Flatten the arrays to map a uniform spatial grid layout
        flat_x = x_mesh.flatten()
        flat_y = y_mesh.flatten()

        # Calculate bounding coordinates around centers [X_min, Y_min, X_max, Y_max]
        half_scale = self.base_scale // 2
        anchors = np.vstack([
            flat_x - half_scale,
            flat_y - half_scale,
            flat_x + half_scale,
            flat_y + half_scale
        ]).T

        return anchors.astype(np.int32)

# 1. Simulate 3 sample horizontal and vertical coordinate tracking grid center stripes
mock_centers_x = np.array([32, 64, 96])
mock_centers_y = np.array([40, 80, 120])

print("Step 1: Simulated Camera Grid Center Arrays:")
print(f"X-Centers: {mock_centers_x}")
print(f"Y-Centers: {mock_centers_y}")
print("-" * 50)

# 2. Run the anchor configuration engine
generator = FeatureAnchorGenerator(base_scale=16)
generated_anchors = generator.generate_spatial_anchors(mock_centers_x, mock_centers_y)

print(f"Step 2: Generated Anchor Coordinate Tensors ({len(generated_anchors)} Unique Windows):")
print("[ X_min  Y_min  X_max  Y_max ]")
print(generated_anchors)
print("\n(Notice: The matrix generated perfect reference frames across the grid!)")
print("=================================================")