import time

print("=================================================")
print("BLURRY FRAME DETECTION QUALITY FILTER ACTIVE")
print("=================================================")

class FrameQualityFilter:
    def __init__(self, blur_threshold=100.0):
        # A Laplacian variance score below this threshold indicates an unstable, blurry image
        self.blur_threshold = blur_threshold
        # Simulated stream frame buffers with calculated clarity scores
        self.incoming_frames = [
            {"frame_id": "cap_0941_1", "variance_score": 142.5},  # Sharp frame
            {"frame_id": "cap_0941_2", "variance_score": 45.2},   # Motion blur frame
            {"frame_id": "cap_0941_3", "variance_score": 118.8}   # Sharp frame
        ]

    def evaluate_frame_clarity(self, frame_data):
        print(f"[FILTER] Analyzing matrix sharpness profile for: '{frame_data['frame_id']}'...")
        time.sleep(0.3)  # Simulate computing the variance of Laplacian matrix kernels
        
        print(f" -> Computed Clarity Score: {frame_data['variance_score']:.1f} (Threshold: {self.blur_threshold})")
        
        if frame_data["variance_score"] >= self.blur_threshold:
            print(" -> [STATUS: PASSED] Frame is sharp. Forwarding to face recognition array.")
            return True
        else:
            print(" -> [STATUS: DROPPED] High motion blur detected! Discarding frame matrix to optimize CPU.")
            return False

    def run_pipeline_pass(self):
        for frame in self.incoming_frames:
            self.evaluate_frame_clarity(frame)
            print("-" * 55)

# 1. Initialize the frame quality filter engine
quality_filter = FrameQualityFilter()
quality_filter.run_pipeline_pass()

print("=================================================")