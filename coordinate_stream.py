import numpy as np
import time

print("=================================================")
print("📹 LIVE CAMERA COORDINATE STREAM BUFFER ACTIVE 📹")
print("=================================================")

class CoordinateStreamBuffer:
    def __init__(self, buffer_size=4):
        self.buffer_size = buffer_size
        self.buffer = np.zeros((self.buffer_size, 2), dtype=np.float32)
        self.pointer = 0
        self.total_frames_tracked = 0

    def update_coordinates(self, new_x, new_y):
        self.buffer[self.pointer] = [new_x, new_y]
        self.pointer = (self.pointer + 1) % self.buffer_size
        self.total_frames_tracked += 1

        print(f"[FRAME #{self.total_frames_tracked:02d}] Real-time Centroid Detected: ({new_x:.1f}, {new_y:.1f})")

    def get_rolling_history(self):
        return self.buffer

stream_tracker = CoordinateStreamBuffer(buffer_size=4)

simulated_detections = [
    (120.5, 340.2),
    (122.1, 341.0),
    (125.8, 339.4),
    (128.2, 342.1),
    (131.0, 345.6),
]

print("🚀 Simulating live streaming spatial coordinates inputs...")
print("-" * 50)

for x, y in simulated_detections:
    stream_tracker.update_coordinates(x, y)

print("-" * 50)
print("📊 Current Rolling Memory Matrix (Last 4 Frames Kept):")
print(stream_tracker.get_rolling_history())
print("\n(Notice: The oldest coordinate was dropped automatically to prevent RAM leakage!)")
print("=================================================")