student_database = np.array([
    [3.2,5.1,5.0],
    [2.8,4.9,42.5],
    [3.5,5.5,48.2]
])
live_scan = np.array([2.9,4.8,42.8])
print(f"\n[SCAN] Live Feature Tracking Array Vector: {live_scan}")
distances = np.sqrt(np.sum((student_database - live_scan) ** 2,axis=1))
print("\n Calculating vector distances to database records...")
for i, dist in enumerate(distances):
    print(f"-> Distance to Student Index #{i}: {dist:.4f}")
closest_student_idx = np.argmin(distances)
print("-"*50)
print(f"MATCH FOUND: Live scan matches Student Index #{closest_student_idx}!")
print(f"Access Granted. Attendence logged for index #{closest_student_idx}.")
print("==============================================================")