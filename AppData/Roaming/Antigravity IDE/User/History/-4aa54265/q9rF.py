import numpy as np

print("=================================================")
print("LIVENESS DETECTION TEXTURE PROFILER ACTIVE")
print("=================================================")

class LivenessDetector:
    def __init__(self, variance_threshold=15.0):
        # High texture variance indicates natural 3D depth and shadows
        # Low variance or flat values flag a uniform paper/screen surface
        self.threshold = variance_threshold

    def analyze_surface_texture(self, image_matrix):
        # 1. Compute spatial gradients along x and y axes using differences
        grad_x = np.diff(image_matrix, axis=1)[:, :-1]
        grad_y = np.diff(image_matrix, axis=0)[:-1, :]
        
        # 2. Combine spatial energy magnitudes
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