import numpy as np

print("=================================================")
print("LIVENESS DETECTION TEXTURE PROFILER ACTIVE")
print("=================================================")

class LivenessDetector:
    def __init__(self, variance_threshold=15.0):
        self.threshold = variance_threshold

    def analyze_surface_texture(self, image_matrix):
        # Cast to float to handle differences accurately without unsigned wrap-around bugs
        mat_float = image_matrix.astype(np.float32)
        
        # 1. Calculate structural differences along horizontal and vertical axes
        # To make them broadcastable, slice the opposing dimensions back to an even grid size
        grad_x = np.diff(mat_float, axis=1)[:-1, :]   # Drops a column, manually drop a row
        grad_y = np.diff(mat_float, axis=0)[:, :-1]   # Drops a row, manually drop a column
        
        # 2. Combine tracking spatial energy magnitudes smoothly
        gradient_magnitude = np.sqrt(np.square(grad_x) + np.square(grad_y))
        
        # 3. Compute overall variance of the texture energy matrix
        texture_variance = np.var(gradient_magnitude)
        
        return texture_variance

    def verify_authenticity(self, image_matrix):
        variance = self.analyze_surface_texture(image_matrix)
        print(f"Computed Texture Variance: {variance:.2f}")
        
        if variance >= self.threshold:
            print("Status: AUTHENTIC LIVE SUBJECT")
            return True
        else:
            print("Status: SPOOF ATTEMPT DETECTED (PHOTO/SCREEN)")
            return False

# 1. Initialize detector engine
detector = LivenessDetector(variance_threshold=15.0)

# 2. Simulate a real 4x4 face region with natural texture depth fluctuations
real_face_patch = np.array([
    [120, 45,  190, 80],
    [30,  175, 90,  210],
    [160, 85,  240, 50],
    [70,  220, 110, 135]
], dtype=np.uint8)

# 3. Simulate a flat, reprinted photo patch with very static, uniform reflection
spoof_photo_patch = np.array([
    [100, 102, 101, 100],
    [101, 100, 102, 101],
    [100, 101, 100, 102],
    [102, 100, 101, 100]
], dtype=np.uint8)

print("Analyzing Sample A (Live Camera Stream Input):")
detector.verify_authenticity(real_face_patch)

print("-" * 50)

print("Analyzing Sample B (Printed Document Copy Input):")
detector.verify_authenticity(spoof_photo_patch)
print("=================================================")