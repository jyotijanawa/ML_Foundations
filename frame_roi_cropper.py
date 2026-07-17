import time

print("=================================================")
print("DYNAMIC FRAME REGION OF INTEREST CROPPER ACTIVE")
print("=================================================")

class FrameROICropper:
    def __init__(self):
        # Simulated raw frame matrix size coordinates
        self.canvas_width = 1280
        self.canvas_height = 720

    def extract_face_roi(self, frame_id, bounding_box):
        """
        Simulates cropping out a specific region of interest matrix 
        using boundary coordinate vectors: [x_min, y_min, x_max, y_max]
        """
        x_min, y_min, x_max, y_max = bounding_box
        print(f"[PROCESS] Processing frame source input: '{frame_id}'...")
        time.sleep(0.3)  # Simulate matrix slice allocation delay
        
        # Verify boundary constraints map inside our frame dimensions
        if x_max <= self.canvas_width and y_max <= self.canvas_height:
            roi_width = x_max - x_min
            roi_height = y_max - y_min
            
            print(f" -> Bounding Box Coordinates Isolated: [{x_min}, {y_min}] to [{x_max}, {y_max}]")
            print(f" -> [SLICING] Extracting sub-matrix patch grid size: {roi_width}x{roi_height} pixels.")
            print("[SUCCESS] Face matrix ROI successfully extracted and sent to embedding layer.")
            return True
        else:
            print("[ERROR] Bounding box parameters exceed maximum frame dimension limits!")
            return False

# 1. Initialize the frame cropping module
cropper = FrameROICropper()

# 2. Simulate isolation coordinates for a detected face bounding box area
# Format: [x_min, y_min, x_max, y_max]
mock_face_coordinates = [240, 180, 480, 420]

print("--- Frame Processing Execution Pipeline ---")
cropper.extract_face_roi("live_stream_frame_idx_4", mock_face_coordinates)

print("=================================================")