import time

print("=================================================")
print("REAL-TIME STREAM FPS & LATENCY PROFILER ACTIVE")
print("=================================================")

class StreamFPSProfiler:
    def __init__(self, target_fps=15.0):
        self.target_fps = target_fps
        self.frame_times = []
        self.last_timestamp = None

    def start_frame_clock(self):
        self.last_timestamp = time.perf_counter()

    def record_frame_completion(self, frame_id):
        if self.last_timestamp is None:
            print("[PROFILER] Error: Clock not started before recording completion.")
            return

        now = time.perf_counter()
        elapsed_time = now - self.last_timestamp
        self.last_timestamp = now
        
        self.frame_times.append(elapsed_time)
        
        # Keep moving window of last 5 frames
        if len(self.frame_times) > 5:
            self.frame_times.pop(0)

        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        current_fps = 1.0 / avg_frame_time if avg_frame_time > 0 else 0.0
        latency_ms = elapsed_time * 1000

        print(f"[METRIC] Processed '{frame_id}' | Latency: {latency_ms:.1f} ms | Moving FPS: {current_fps:.2f}")

        if current_fps < self.target_fps:
            print(f" -> [WARNING] Frame rate dropped below threshold target ({self.target_fps} FPS)!")

# 1. Instantiate stream profiler with 15 FPS baseline target
profiler = StreamFPSProfiler(target_fps=15.0)

print("\n--- Simulating Frame Execution Latency Window ---")
# 2. Simulate profiling across a sequence of video frames
mock_latencies = [0.04, 0.05, 0.08, 0.04]  # Simulated latency in seconds

for idx, delay in enumerate(mock_latencies, start=1):
    profiler.start_frame_clock()
    time.sleep(delay)  # Simulate neural network frame inference time
    profiler.record_frame_completion(f"frame_idx_{idx:03d}")

print("-" * 50)
print("[SUCCESS] Stream latency and throughput profiling completed.")
print("=================================================")