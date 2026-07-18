import time

print("=================================================")
print("PIPELINE CORE EXCEPTION HIERARCHY MATRIX ACTIVE")
print("=================================================")

# --- Core Custom Error Inheritance Structure ---

class AttendanceSystemError(Exception):
    """Base exception class for all custom automation pipeline errors."""
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
        self.timestamp = time.strftime("%H:%M:%S")

class CriticalHardwareException(AttendanceSystemError):
    """Raised when a physical resource (like a camera device bus) fails unrecoverably."""
    def __init__(self, message):
        super().__init__(message, error_code="ERR_HW_FATAL")

class AlgorithmicConstraintException(AttendanceSystemError):
    """Raised when data fails runtime accuracy thresholds (like low frame clarity)."""
    def __init__(self, message, metric_value):
        super().__init__(message, error_code="ERR_ALGO_WARN")
        self.metric_value = metric_value

# --- Simulation & Handling Pipeline ---

class ErrorHandlingOrchestrator:
    @staticmethod
    def simulate_pipeline_run(trigger_type):
        print(f"[PIPELINE] Initializing run slice validation for trace: {trigger_type}...")
        time.sleep(0.3)
        
        if trigger_type == "hardware":
            raise CriticalHardwareException("Webcam bus disconnected or power rail failure.")
        elif trigger_type == "algorithm":
            raise AlgorithmicConstraintException("Laplacian variance score dropped below safe metric.", metric_value=42.1)
        else:
            print("[PIPELINE] Execution slice processed with zero core faults.")

# 1. Instantiate the test orchestrator
orchestrator = ErrorHandlingOrchestrator()

# 2. Execute structured try-except blocks to catch the distinct custom objects
for test_case in ["algorithm", "hardware"]:
    try:
        orchestrator.simulate_pipeline_run(test_case)
    except AlgorithmicConstraintException as ex:
        print(f" -> Caught [{ex.error_code}] at {ex.timestamp}: {ex}")
        print(f"    Action: Dynamic Metric Logged -> {ex.metric_value}. Dropping frame window safely.")
    except CriticalHardwareException as ex:
        print(f" -> Caught [{ex.error_code}] at {ex.timestamp}: {ex}")
        print("    Action: Emergency shutdown signal sent to main thread stack.")
    print("-" * 55)

print("=================================================")