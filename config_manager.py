import json
import os

print("=================================================")
print("⚙️ AUTOMATED VISION CONFIGURATION REGISTRY ACTIVE ⚙️")
print("=================================================")

class VisionConfigManager:
    def __init__(self, config_filename="system_config.json"):
        self.config_path = config_filename
        # Default core parameters for our computer vision pipeline
        self.default_settings = {
            "camera_settings": {
                "device_index": 0,
                "frame_width": 640,
                "frame_height": 480,
                "target_fps": 30
            },
            "recognition_thresholds": {
                "face_match_confidence": 0.85,
                "spatial_iou_limit": 0.50
            },
            "storage_paths": {
                "dataset_directory": "./student_database",
                "logs_directory": "./attendance_logs"
            }
        }
        self.current_settings = {}
        self.load_configuration()

    def load_configuration(self):
        # If config file doesn't exist, create it with default matrix structures
        if not os.path.exists(self.config_path):
            print("[INFO] No configuration file found. Initializing factory defaults...")
            self.save_configuration(self.default_settings)
            self.current_settings = self.default_settings
        else:
            print("[INFO] Syncing configuration parameters from disk...")
            with open(self.config_path, "腔", encoding="utf-8") as file:
                # Catch block safely if file is empty or corrupted
                try:
                    self.current_settings = json.load(file)
                except json.JSONDecodeError:
                    self.current_settings = self.default_settings

    def save_configuration(self, settings_data):
        with open(self.config_path, "w", encoding="utf-8") as file:
            json.dump(settings_data, file, indent=4)
        print("[SUCCESS] New configuration matrix mapped safely to storage.")

    def get_setting(self, category, key):
        return self.current_settings.get(category, {}).get(key, None)

# 1. Initialize our system settings registry
config_engine = VisionConfigManager()

print("-" * 50)
print("📋 Active Camera Registration Scale:")
width = config_engine.get_setting("camera_settings", "frame_width")
height = config_engine.get_setting("camera_settings", "frame_height")
print(f"👉 Target Resolution: {width} x {height} Pixels")

print(f"👉 Recognition Target Boundary: {config_engine.get_setting('recognition_thresholds', 'face_match_confidence') * 100}%")
print("=================================================")