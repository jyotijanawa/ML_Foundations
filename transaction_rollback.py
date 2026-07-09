import time

print("=================================================")
print("SYSTEM TRANSACTION ROLLBACK MANAGER ACTIVE")
print("=================================================")

class TransactionRollbackManager:
    def __init__(self):
        # Simulated core database file storage data states
        self.active_ledger_state = ["Roll_301:Present", "Roll_305:Present"]
        self.backup_checkpoint_state = []

    def create_safety_checkpoint(self):
        print("[CHECKPOINT] Backing up stable attendance state matrix...")
        # Create a clean shallow copy clone of the data state array
        self.backup_checkpoint_state = list(self.active_ledger_state)
        time.sleep(0.3)
        print(f" -> Snapshot saved. Rows protected: {len(self.backup_checkpoint_state)}")

    def apply_ledger_modifications(self, simulated_crash=False):
        self.create_safety_checkpoint()
        print("\n[TRANSACTION] Attempting to write new attendance batches to file...")
        time.sleep(0.4)
        
        try:
            # Modify active working state data array
            self.active_ledger_state.append("Roll_312:Present")
            
            if simulated_crash:
                # Force trigger an I/O writing loop crash error halfway
                raise IOError("Storage write fault: Sudden hardware device disconnect detected.")
                
            print("[SUCCESS] Transaction committed perfectly. Closing file stream safely.")
            self.backup_checkpoint_state = [] # Clear backup cache allocation
            
        except IOError as error:
            print(f"[CRITICAL ERROR] {error}")
            self.execute_abort_and_rollback()

    def execute_abort_and_rollback(self):
        print("[ROLLBACK ENGAGED] Initiating systemic database recovery sequence...")
        time.sleep(0.5)
        
        # Discard the broken state and completely restore the original checkpoint array
        self.active_ledger_state = list(self.backup_checkpoint_state)
        print("[RECOVERED] Corrupted lines dropped. Database state reverted to safe point.")
        print(f" -> Active Safe Data State: {self.active_ledger_state}")

# 1. Initialize the rollback manager node
manager = TransactionRollbackManager()

# 2. Run a clean, normal transaction update sequence
print("--- Transaction Scenario A: Clean File Update ---")
manager.apply_ledger_modifications(simulated_crash=False)

print("-" * 55)

# 3. Run a faulty transaction sequence where an unexpected error triggers rollback
print("--- Transaction Scenario B: System Fault Recovery ---")
manager.apply_ledger_modifications(simulated_crash=True)

print("=================================================")