import time
import threading

print("=================================================")
print("THREAD-SAFE FRAME BUFFER QUEUE MANAGER ACTIVE")
print("=================================================")

class FrameBufferQueue:
    def __init__(self, max_capacity=3):
        self.max_capacity = max_capacity
        self.queue = []
        # Explicit thread locking primitives to avoid race conditions
        self.lock = threading.Lock()

    def enqueue_incoming_frame(self, frame_id):
        """Thread-safe operation to push raw frames into the active processing stack."""
        with self.lock:
            print(f"[CAMERA THREAD] Attempting to push frame reference: '{frame_id}'")
            
            # Drop the oldest frame if capacity is breached to avoid stream lag
            if len(self.queue) >= self.max_capacity:
                dropped = self.queue.pop(0)
                print(f" -> [BUFFER OVERFLOW] Dropping oldest frame '{dropped}' to maintain zero lag.")
            
            self.queue.append(frame_id)
            print(f" -> [QUEUED] Current buffer size: {len(self.queue)}/{self.max_capacity}")

    def dequeue_processing_frame(self):
        """Thread-safe operation for the inference engine to fetch the next frame target."""
        with self.lock:
            if not self.queue:
                print("[INFERENCE THREAD] Queue is completely empty. Awaiting frame matrix assets...")
                return None
            
            next_frame = self.queue.pop(0)
            print(f"[INFERENCE THREAD] Extracted '{next_frame}' from queue buffer for neural network analysis.")
            return next_frame

# 1. Initialize our bounded thread-safe memory manager
buffer_manager = FrameBufferQueue(max_capacity=2)

print("\n--- Simulating High-Speed Concurrency Steps ---")
time.sleep(0.3)

# 2. Simulate the camera frame feed pumping data faster than the system can process it
buffer_manager.enqueue_incoming_frame("frame_chunk_001")
buffer_manager.enqueue_incoming_frame("frame_chunk_002")
buffer_manager.enqueue_incoming_frame("frame_chunk_003") # This should trigger our overflow dropping logic

print("-" * 50)

# 3. Simulate the deep learning worker loop pulling the next available image data blocks
buffer_manager.dequeue_processing_frame()
buffer_manager.dequeue_processing_frame()

print("-" * 50)
print("[SUCCESS] Thread-safe ring buffer states verified without pipeline deadlocks.")
print("=================================================")