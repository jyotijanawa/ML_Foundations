import hashlib
import time

print("=================================================")
print("ADMINISTRATIVE PANEL GATEKEEPER MODULE ACTIVE")
print("=================================================")

class AdminGatekeeper:
    def __init__(self):
        # Simulation of a securely stored password hash (SHA-256 for 'MDU_CSE_2026')
        self._stored_hash = "6798e9477fd03dc8ea0e8df4567c2937be199e8d47be40b991da3b27cf1722e1"
        self.session_authenticated = False

    def verify_credentials(self, input_password):
        """Hashes the input password and checks it against the secure stored hash."""
        # Convert input string to bytes and compute SHA-256 hash
        input_hash = hashlib.sha256(input_password.encode()).hexdigest()
        
        if input_hash == self._stored_hash:
            self.session_authenticated = True
            print("\n[SUCCESS] Authentication verified. Access granted to core settings.")
            return True
        else:
            self.session_authenticated = False
            print("\n[DENIED] Invalid security passphrase. Access blocked.")
            return False

    def launch_admin_dashboard(self):
        """Simulates administrative actions once authenticated."""
        if not self.session_authenticated:
            print("[ERROR] Unauthorized access attempt blocked. Action logged.")
            return
            
        print("\n--- WELCOME TO THE ATTENDANCE MANAGEMENT PORTAL ---")
        print("Available Administrative Actions:")
        print(" [1] Register New Student Face Vectors")
        print(" [2] Modify Period Timetable Slots")
        print(" [3] Force Manual Ledger Push to Cloud Server")
        print(" [4] Exit Administrative Session")
        print("-" * 50)
        print("[INFO] Portal operating securely.")

# 1. Initialize the system gateway
gatekeeper = AdminGatekeeper()

# 2. Simulate an unauthorized attempt
print("--- Execution Run A: Testing Security Lockout ---")
gatekeeper.verify_credentials("WrongPassword123")
gatekeeper.launch_admin_dashboard()

print("-" * 50)

# 3. Simulate an authorized access routine
print("--- Execution Run B: Testing Verified Entry ---")
# The correct phrase that matches the hash is 'MDU_CSE_2026'
gatekeeper.verify_credentials("MDU_CSE_2026")
gatekeeper.launch_admin_dashboard()

print("=================================================")