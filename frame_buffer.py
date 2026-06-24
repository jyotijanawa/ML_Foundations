import collections
import time
import numpy as np

print("=================================================")
print("STREAMING VIDEO FRAME BUFFER REGISTRY ACTIVE")
print("=================================================")

class VideoFrameBuffer:
    def __init__(self, max_buffer_size=3):
        # Using collections.deque with maxlen automatically drops old frames
        # when new ones arrive, keeping memory usage constant.
        self.buffer = collections.deque(maxlen=max_buffer_size)

    def enqueue_camera_frame(self, frame_matrix):
        # Push a raw frame array into the buffer stack
        self.buffer.append(frame_matrix)

    def dequeue_latest_frame(self):
        if len(self.buffer) == 0:
            print("Buffer Status: Empty")
            return None
        
        # Pop the newest available frame for immediate model processing
        # This prevents lag by discarding older intermediate frames
        latest_frame = self.buffer.pop()
        self.buffer.clear() # Clear out anything older remaining in queue
        return latest_frame

    def get_current_backlog_size(self):
        return len(self.buffer)

# 1. Initialize our streaming buffer matrix tracking up to 3 frames max
stream_buffer = VideoFrameBuffer(max_buffer_size=3)

# 2. Simulate 4 incoming consecutive camera frame captures
# Each frame is a mock 2x2 image patch matrix
frame_time_1 = np.array([[10, 11], [12, 13]], dtype=np.uint8)
frame_time_2 = np.array([[14, 15], [16, 17]], dtype=np.uint8)
frame_time_3 = np.array([[18, 19], [20, 21]], dtype=np.uint8)
frame_time_4 = np.array([[22, 23], [24, 25]], dtype=np.uint8)

print("Ingesting frames from camera stream feed...")
stream_buffer.enqueue_camera_frame(frame_time_1)
stream_buffer.enqueue_camera_frame(frame_time_2)
stream_buffer.enqueue_camera_frame(frame_time_3)
# Frame 4 arrives before the model finishes processing, bumping out Frame 1
stream_buffer.enqueue_camera_frame(frame_time_4)

print(f"Current Frame Backlog Queue Count: {stream_buffer.get_current_backlog_size()}")
print("-" * 50)

# 3. Pull the absolute newest frame for the neural network model processing loop
print("Model request: Fetching freshest frame context...")
active_processing_tensor = stream_buffer.dequeue_latest_frame()

print("Active Processing Frame Output Matrix Matrix:")
print(active_processing_tensor)
print("\n(Notice: The matrix returned frame 4, successfully skipping old lag!)")
print("=================================================")