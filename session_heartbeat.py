import time

print("=================================================")
print("ACTIVE SESSION KEEP-ALIVE HEARTBEAT ACTIVE")
print("=================================================")

class SessionHeartbeatEmitter:
    def __init__(self, room_id="Lab-303", target_interval=3):
        self.room_id = room_id
        self.interval = target_interval
        self.pulse_count = 0

    def start_heartbeat_loop(self, max_pulses=3):
        print(f"[INITIALIZE] Starting background heartbeat service for Room: {self.room_id}")
        print(f"[INITIALIZE] Pulse ping frequency configured to every {self.interval} seconds.")
        print("-" * 55)
        
        while self.pulse_count < max_pulses:
            self.pulse_count += 1
            timestamp = time.strftime("%H:%M:%S")
            
            # Simulate emitting a payload containing system status
            print(f"[{timestamp}] [HEARTBEAT] Sending Pulse #{self.pulse_count}...")
            time.sleep(0.3) # Simulate network transmission latency
            print(f" -> Response: Central Server acknowledged pulse. Status: HEALTHY")
            
            if self.pulse_count < max_pulses:
                # Wait for the next interval wave
                time.sleep(self.interval - 0.3)
                
        print("-" * 55)
        print("[STATUS] Keep-alive simulation interval loop completed successfully.")

# 1. Initialize the heartbeat daemon for your classroom lab station
emitter = SessionHeartbeatEmitter(room_id="MDU-CSE-LAB4")
emitter.start_heartbeat_loop(max_pulses=3)

print("=================================================")