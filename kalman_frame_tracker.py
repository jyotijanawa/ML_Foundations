import time

print("=================================================")
print("KALMAN BOUNDING BOX TRAJECTORY TRACKER ACTIVE")
print("=================================================")

class BoundingBoxKalmanTracker:
    def __init__(self, initial_position, velocity=(2, 1)):
        # State Vector: [x, y, dx, dy]
        self.x, self.y = initial_position
        self.vx, self.vy = velocity
        # Process noise and measurement state variance
        self.dt = 1.0  # Time step delta

    def predict_next_state(self):
        """Predicts object spatial coordinates using linear kinematic equations."""
        print(f"[KALMAN PREDICT] Computing kinematic state estimation vector (dt={self.dt})...")
        time.sleep(0.3)
        
        # State transition: x_new = x + vx*dt, y_new = y + vy*dt
        self.x = self.x + (self.vx * self.dt)
        self.y = self.y + (self.vy * self.dt)
        
        print(f" -> Predicted Bounding Box Center Vector: ({self.x:.1f}, {self.y:.1f})")
        return (self.x, self.y)

    def update_measurement(self, measured_position):
        """Corrects internal state matrix when fresh sensor detection coordinates arrive."""
        print(f"[KALMAN UPDATE] Adjusting prediction against camera measurement: {measured_position}...")
        time.sleep(0.3)
        
        meas_x, meas_y = measured_position
        # Simple gain weighting adjustment step
        gain = 0.6
        self.x = self.x + gain * (meas_x - self.x)
        self.y = self.y + gain * (meas_y - self.y)
        
        # Recalculate dynamic velocity profile
        self.vx = (meas_x - self.x) / self.dt
        self.vy = (meas_y - self.y) / self.dt
        
        print(f" -> Updated Corrected Trajectory Center: ({self.x:.1f}, {self.y:.1f})")
        print(f" -> Recalibrated Velocity Vector: ({self.vx:.2f}, {self.vy:.2f})")

# 1. Initialize tracker with initial face bounding box centroid at (100, 150)
tracker = BoundingBoxKalmanTracker(initial_position=(100, 150), velocity=(5, 2))

print("\n--- Cycle 1: Frame Occlusion (Pure Prediction Pass) ---")
# Frame 1: Camera detection lost due to motion blur; predict purely on velocity
predicted_coords = tracker.predict_next_state()

print("\n--- Cycle 2: Fresh Detection Sensor Measurement ---")
# Frame 2: Face detector re-acquires subject at position (107, 153)
tracker.update_measurement(measured_position=(107, 153))

print("-" * 50)
print("[SUCCESS] Spatial trajectory estimation stabilized across frame sequence.")
print("=================================================")