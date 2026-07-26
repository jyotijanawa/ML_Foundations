import time
import math

print("=================================================")
print("ADAPTIVE LOGIT TEMPERATURE SCALER ACTIVE")
print("=================================================")

class LogitTemperatureScaler:
    def __init__(self, temperature=1.5):
        # Temperature hyperparameter T > 1.0 smooths overconfident predictions
        self.temperature = temperature

    def softmax(self, logits):
        """Computes numerically stable softmax probabilities."""
        max_logit = max(logits)
        exp_logits = [math.exp(z - max_logit) for z in logits]
        sum_exp = sum(exp_logits)
        return [e / sum_exp for e in exp_logits]

    def calibrate_confidence(self, raw_logits):
        print(f"[CALIBRATION] Applying logit scaling factor (Temperature T = {self.temperature})...")
        time.sleep(0.4)  # Simulate forward-pass logit transformation
        
        # Calculate raw unscaled probabilities
        raw_probs = self.softmax(raw_logits)
        
        # Scale logits: z_scaled = z / T
        scaled_logits = [z / self.temperature for z in raw_logits]
        calibrated_probs = self.softmax(scaled_logits)
        
        print("\n--- Model Calibration Telemetry ---")
        print(f" -> Raw Input Logits     : {raw_logits}")
        print(f" -> Raw Softmax Probs    : {[round(p, 4) for p in raw_probs]}")
        print(f" -> Calibrated Probs (T) : {[round(p, 4) for p in calibrated_probs]}")
        print("-" * 50)
        
        peak_diff = max(raw_probs) - max(calibrated_probs)
        print(f"[SUCCESS] Overconfidence dampened by {peak_diff * 100:.2f}%. Distribution smoothed cleanly.")
        return calibrated_probs

# 1. Instantiate temperature scaler with T = 1.5
scaler = LogitTemperatureScaler(temperature=1.5)

# 2. Simulate raw output logits for 3 student identity classes [Roll_301, Roll_305, Roll_312]
# High raw logit creates extreme overconfidence in standard softmax
raw_identity_logits = [5.2, 1.1, -0.8]

scaler.calibrate_confidence(raw_identity_logits)

print("=================================================")