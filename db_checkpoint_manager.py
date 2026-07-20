import time

print("=================================================")
print("DATABASE STATE ROLLBACK CHECKPOINTER ACTIVE")
print("=================================================")

class DBCheckpointManager:
    def __init__(self):
        # Master table state representing total present counts for a course block
        self.master_ledger_state = {"301": 26, "305": 28, "312": 21}
        self.checkpoint_cache = {}
        self.transaction_open = False

    def create_atomic_checkpoint(self):
        print("[CHECKPOINT] Backing up current master records into volatile cache memory...")
        time.sleep(0.4)  # Simulate writing state to checkpoint logs
        self.checkpoint_cache = self.master_ledger_state.copy()
        self.transaction_open = True
        print(f" -> Snapshot Saved: {self.checkpoint_cache}")

    def apply_bulk_updates(self, updates_batch):
        if not self.transaction_open:
            print("[ERROR] Cannot apply updates without an open transaction checkpoint!")
            return False
            
        print("\n--- Processing Transaction Batch Writes ---")
        try:
            for roll_id, addition in updates_batch.items():
                print(f" -> Writing target updates to key: {roll_id} (+{addition})")
                time.sleep(0.2)
                
                # Intentional strict constraint: simulate a failure if unexpected structural data is written
                if int(roll_id) > 400:
                    raise ValueError(f"Invalid Roll Index Allocation: {roll_id}")
                    
                self.master_ledger_state[roll_id] = self.master_ledger_state.get(roll_id, 0) + addition
                
            print("[SUCCESS] All database writes committed to memory cleanly.")
            self.transaction_open = False
            return True
            
        except Exception as error:
            print(f"\n[CRITICAL FAULT ENCOUNTERED] Reason: {error}")
            self.abort_and_rollback()
            return False

    def abort_and_rollback(self):
        print("[ROLLBACK] Initiating system restore sequence...")
        time.sleep(0.5)  # Simulate pulling back historical checkpoint blocks
        self.master_ledger_state = self.checkpoint_cache.copy()
        print(f"[STATUS] Master ledger cleanly reverted to safe checkpoint state: {self.master_ledger_state}")
        self.transaction_open = False

# 1. Initialize the storage checkpointer engine
manager = DBCheckpointManager()

# 2. Open a transaction and attempt a faulty batch write simulation
manager.create_atomic_checkpoint()
faulty_batch = {"301": 1, "405": 1}  # 405 will trigger the validation error constraint

manager.apply_bulk_updates(faulty_batch)

print("=================================================")