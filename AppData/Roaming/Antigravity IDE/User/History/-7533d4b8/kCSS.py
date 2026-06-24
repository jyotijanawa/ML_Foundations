import numpy as np
import time
from config_manager import VisionConfigManager
from image_preprocessor import ImagePreprocessor
from matrixs_monitor import PerformanceMonitor
print("=================================================")
print("MATRIX VISION PIPELINE COORDINATOR ACTIVE")
print("=================================================")
class VisionPipelineCoordinator:
    def __init__(self):
        print("[INIT] Initializing unified vision subsystems...")
        self.config = VisionConfigManager()
        self.preprocessor = ImagePreprocessor()
        self.monitor = PerformanceMonitor(fps_warning_threshold=25.0)
    def process_incoming_frame(self, raw_frame_matrix):
        start_time = time.time()
        print("\n[FRAME RECEIVED] Directing through processing sequence...")
        target_width = self.config.get_setting("camera_settings", "frame_width")
        print(f"Target validation matrix width check: {target_width}px")
        print("Processing spatial normalizations...")
        processed_tensor = self.preprocessor.standardize_matrix(raw_frame_matrix)
        time.sleep(0.035)
        end_time = time.time()
        total_latency = end_time - start_time
        self.monitor.log_frame_processing_time(total_latency)
        print("[SUCCESS] Frame processed completely.")
        return processed_tensor
pipeline = VisionPipelineCoordinator()
mock_raw_frame = np.array([
    [140, 155, 170],
    [90, 110, 135],
    [45, 60, 85]
], dtype=np.uint8)
final_output = pipeline.process_incoming_frame(mock_raw_frame)
print("-" * 50)
print("Final Operational Diagnostics Snapshot:")
pipeline.monitor.generate_analytics_report()
print("=================================================")