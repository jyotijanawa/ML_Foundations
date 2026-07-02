import hashlib
import time

print("=================================================")
print("ENCRYPTED LEDGER SECURITY HASH VAULT ACTIVE")
print("=================================================")

class LedgerHasher:
    def __init__(self):
        # Emulating the text data contents of a standard class session ledger
        self.original_ledger_data = "Course:CSE-304G,Roll:301:Present,Roll:305:Present,Roll:312:Present"
        self.tampered_ledger_data = "Course:CSE-304G,Roll:301:Present,Roll:305:Present,Roll:312:Present,Roll:320:Present" # Added roll 320 manually
        self.secure_signature = ""

    def generate_security_signature(self):
        print("[PROCESS] Compiling text strings from active ledger...")
        time.sleep(0.4)
        
        # Generating a unique cryptographic SHA-256 hash token based on the content
        self.secure_signature = hashlib.sha256(self.original_ledger_data.encode()).hexdigest()
        print(f"[SUCCESS] Digital seal generated for today's records.")
        print(f" -> Seal Signature: {self.secure_signature}")

    def verify_ledger_integrity(self, file_content_to_check):
        print("\n[SECURITY Check] Scanning file structure against original digital seal...")
        time.sleep(0.5)
        
        # Re-compute hash of the data being checked
        check_hash = hashlib.sha256(file_content_to_check.encode()).hexdigest()
        
        if check_hash == self.secure_signature:
            print("[STATUS: PASSED] Digital seal matches completely. File data is authentic and safe.")
            return True
        else:
            print("[STATUS: CRITICAL ALARM] Cryptographic mismatch detected!")
            print(" -> [WARNING] The ledger data has been modified or tampered with externally!")
            return False

# 1. Initialize the cryptographic security utility
vault = LedgerHasher()

# 2. Seal the official data
print("--- Step 1: Sealing Today's Official Attendance File ---")
vault.generate_security_signature()
print("-" * 50)

# 3. Test a clean validation run
print("--- Step 2: Running Verification on Unmodified File ---")
vault.verify_ledger_integrity(vault.original_ledger_data)
print("-" * 50)

# 4. Test an altered validation run
print("--- Step 3: Running Verification on Tampered/Altered File ---")
vault.verify_ledger_integrity(vault.tampered_ledger_data)

print("=================================================")