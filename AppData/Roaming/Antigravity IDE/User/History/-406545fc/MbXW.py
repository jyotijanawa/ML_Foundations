import numpy as np
print("=============================================")
print("COMPUTER VISION ATTENDANE ENGINE INITIALIZING")
print("=============================================")
camera_frame = np.array([
    [10,12,15,12,10],
    [11,240,245,242,12],
    [14,238,255,239,15],
    [12,241,24,240,11],
    [10,15,12,11,13]
])
print("\n[INFO] Simulated Raw Camera Grayscale Matrix:")
print(camera_frame)
print("-"*50)
thresold_value = 150
binary_face_mask = (camera_frame > thresold_value).astype(int)
print(f"\n(Note: '1' represents detected facial features, '0' is bacground)")
print("-"*50)
face_coordinates = np.argwhere(binary_face_mask == 1)
print("Extracting Features Tracking Coordinate:")
for point in face_coordinates:
    print(f"-> Human Feature Pixel Locates at Matrix Position: Row {point[0]}, Col {point[1]}")
print("===================================================")