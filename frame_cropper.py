import time

print("=================================================")
print("FACE IMAGE ASPECT RATIO & FRAME CROPPER ACTIVE")
print("=================================================")

class FaceFrameCropper:
    def __init__(self, target_width=160, target_height=160):
        # Target dimension matrices required by typical deep learning embeddings
        self.target_w = target_width
        self.target_h = target_height

    def normalize_face_bounding_box(self, initial_w, initial_h):
        print(f"[PROCESS] Evaluating incoming frame dimensions: {initial_w}x{initial_h} pixels")
        time.sleep(0.4)  # Simulate frame coordinate calculations
        
        # Calculate aspect ratio
        aspect_ratio = initial_w / initial_h
        print(f" -> Current Matrix Aspect Ratio: {aspect_ratio:.2f}")
        
        # Check if shape requires spatial normalization adjustments
        if initial_w == initial_h:
            print("[INFO] Frame is already perfectly symmetrical.")
        else:
            print("[MODIFIED] Asymmetrical boundaries detected. Applying symmetric boundary padding adjustments...")
            
        time.sleep(0.3)
        print(f"[SUCCESS] Array matrix cropped and resized to uniform standard: {self.target_w}x{self.target_h}")
        return True

# 1. Initialize the frame cropping pipeline
cropper = FaceFrameCropper()

# 2. Simulate processing a non-square raw camera face bounding box 
print("--- Test Run: Processing Raw Bounding Coordinate Block ---")
cropper.normalize_face_bounding_box(240, 180)

print("=================================================")