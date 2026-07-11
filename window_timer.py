import time

print("=================================================")
print("DYNAMIC CHECK-IN WINDOW EXPIRY TIMER ACTIVE")
print("=================================================")

class CheckinWindowTimer:
    def __init__(self, grace_period_minutes=15):
        self.grace_period = grace_period_minutes
        # Simulating minutes passed since the professor initiated the lecture
        self.simulated_elapsed_stages = [4, 11, 18] 

    def evaluate_window_status(self, elapsed_minutes):
        print(f"[TIMER] Checking gate status... Time elapsed: {elapsed_minutes} mins.")
        time.sleep(0.3) # Simulate system clock synchronization
        
        remaining = self.grace_period - elapsed_minutes
        
        if remaining > 0:
            print(f" -> [STATUS: OPEN] {remaining} minutes remaining for valid attendance logging.")
            return True
        else:
            print(f" -> [STATUS: LOCKED] Grace period exceeded by {abs(remaining)} minutes!")
            print("    [ACTION] Rejecting further face recognition inputs for this session.")
            return False

    def run_timer_checks(self):
        for stage in self.simulated_elapsed_stages:
            self.evaluate_window_status(stage)
            print("-" * 50)
            time.sleep(0.2)

# 1. Initialize the check-in window gate keeper
timer_node = CheckinWindowTimer()
timer_node.run_timer_checks()

print("=================================================")