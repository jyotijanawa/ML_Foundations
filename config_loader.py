import time

print("=================================================")
print("PIPELINE PARAMETER CONFIGURATION MANAGER ACTIVE")
print("=================================================")

class PipelineConfigLoader:
    def __init__(self):
        # Default global operational settings for the Deep Learning Pipeline
        self.config_registry = {
            "face_match_threshold": 0.60,      # Strictness of matrix distance verification
            "camera_stream_width": 1280,       # Frame resolution width
            "camera_stream_height": 720,       # Frame resolution height
            "anti_spoofing_enabled": True,     # Texture validation flag
            "server_sync_interval_secs": 15    # Network backup interval rate
        }

    def load_environment_overrides(self):
        print("[PROCESS] Initializing operational environment validation scans...")
        time.sleep(0.4)
        print("[INFO] Loading core algorithmic configurations:")
        for parameter, value in self.config_registry.items():
            print(f"  -> {parameter.ljust(26)} : {value}")

    def update_parameter(self, parameter, new_value):
        """Allows dynamic adjustment of settings during execution loops."""
        if parameter in self.config_registry:
            self.config_registry[parameter] = new_value
            print(f"\n[MODIFIED] Parameter '{parameter}' updated live to: {new_value}")
        else:
            print(f"\n[REJECTED] Parameter '{parameter}' does not exist in system structural configuration.")

# 1. Initialize the configuration infrastructure
config = PipelineConfigLoader()
config.load_environment_overrides()

# 2. Simulate adjustments (e.g., matching a professor's requirement for lower accuracy tolerance)
config.update_parameter("face_match_threshold", 0.55)
config.update_parameter("anti_spoofing_enabled", False)

print("=================================================")