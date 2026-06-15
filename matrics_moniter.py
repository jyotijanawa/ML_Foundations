import time
import numpy as np

print("=================================================")
print("📊 COMPUTER VISION REAL-TIME PERFORMANCE LOG 📊")
print("=================================================")

class PerformanceMonitor:
    def __init__(self, fps_warning_threshold=24.0):
        self.threshold = fps_warning_threshold
        self.frame_latencies = []

    def log_frame_processing_time(self, processing_time_seconds):
        # Accumulate structural processing times in seconds
        self.frame_latencies.append(processing_time_seconds)

    def generate_analytics_report(self):
        if not self.frame_latencies:
            print("[WARN] No processing data captured.")
            return

        # Calculate average processing latency using NumPy vector mean
        avg_latency = np.mean(self.frame_latencies)
        
        # Calculate active Frames Per Second (Math: FPS = 1 / Latency)
        current_fps = 1.0 / avg_latency if avg_latency > 0 else 0.0

        print(f"⏱️ Avg Latency Per Frame : {avg_latency * 1000:.2f} milliseconds")
        print(f"🎬 Active Pipeline Output : {current_fps:.1f} FPS")
        print("-" * 50)

        # 4. Trigger alert systems if system processing degrades below threshold
        if current_fps < self.threshold:
            print(f"⚠️ [PERFORMANCE ALERT]: Frame rate dropped below benchmark ({self.threshold} FPS)!")
            print("👉 Recommendation: Reduce face classification resolution scale or optimize matrix strides.")
        else:
            print("✅ [SYSTEM HEALTH EXCELLENT]: Pipeline streaming within stable performance limits.")

# 1. Initialize monitor with a standard target benchmark of 24 FPS
monitor = PerformanceMonitor(fps_warning_threshold=24.0)

# 2. Simulate the processing times of 5 consecutive face recognition frame runs
# (Varying processing delays in fractions of a second)
simulated_processing_delays = [0.031, 0.035, 0.042, 0.038, 0.045]

print("⚙️ Processing incoming camera frame batches...")
for execution_delay in simulated_processing_delays:
    # Mimic active script computation hold
    time.sleep(0.01) 
    monitor.log_frame_processing_time(execution_delay)

# 3. Output evaluation dashboard metrics
monitor.generate_analytics_report()
print("=================================================")