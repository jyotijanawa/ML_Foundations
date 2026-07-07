import time

print("=================================================")
print("CLASSROOM SESSION STATE CONTROLLER ACTIVE")
print("=================================================")

class SessionStateController:
    def __init__(self):
        # Valid states: 'IDLE', 'ACTIVE_SCANNING', 'FINALIZING', 'CLOSED'
        self.current_state = "IDLE"
        self.active_course = None

    def transition_to(self, new_state):
        print(f"[STATE MACHINE] Attempting transition: {self.current_state} -> {new_state}")
        time.sleep(0.3)  # Simulate state safety checks
        self.current_state = new_state
        print(f"[STATUS] System state successfully updated to: {self.current_state}")

    def start_lecture_session(self, course_code):
        print(f"\n[ORCHESTRATOR] Initializing new classroom session request...")
        self.active_course = course_code
        print(f" -> Targeted Course Target: {self.active_course}")
        
        # Fire up the camera scanning pipeline state
        self.transition_to("ACTIVE_SCANNING")
        print(f"[INFO] Bounding box frames and deep learning pipelines are now drawing power.")

    def terminate_lecture_session(self):
        print(f"\n[ORCHESTRATOR] Timer threshold reached. Winding down session for {self.active_course}...")
        
        # Move to final database write stage
        self.transition_to("FINALIZING")
        time.sleep(0.2)  # Emulate closing file pointers safely
        
        # Bring system down to safe standby mode
        self.transition_to("CLOSED")
        self.active_course = None
        print("[INFO] Camera stream released. System is safely drawing 0% processing load.")

# 1. Initialize the central state engine
controller = SessionStateController()

# 2. Simulate the arrival of a class period (e.g., Advanced Java block)
print("--- Phase 1: Professor Launches Class Period ---")
controller.start_lecture_session("PCC-CSE-304G")

print("-" * 55)

# 3. Simulate the automatic bell/timer closing out the session
print("--- Phase 2: Class Period Time Ends ---")
controller.terminate_lecture_session()

print("=================================================")