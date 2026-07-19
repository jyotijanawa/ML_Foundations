import time

print("=================================================")
print("DYNAMIC LEARNING RATE DECAY SCHEDULER ACTIVE")
print("=================================================")

class StepDecayScheduler:
    def __init__(self, initial_lr=0.01, drop_factor=0.5, epochs_drop=5):
        self.base_lr = initial_lr
        self.drop_factor = drop_factor
        self.epochs_drop = epochs_drop

    def compute_epoch_lr(self, current_epoch):
        """Calculates decayed learning rate based on step intervals."""
        # Calculate how many decay steps have occurred
        decay_steps = current_epoch // self.epochs_drop
        
        # Apply factor scaling: lr = base_lr * (drop_factor ^ decay_steps)
        current_lr = self.base_lr * (self.drop_factor ** decay_steps)
        return current_lr

# 1. Initialize the scheduler with specific optimization boundaries
scheduler = StepDecayScheduler(initial_lr=0.01, drop_factor=0.5, epochs_drop=3)

print("[OPTIMIZER] Beginning learning rate scheduling simulation pass...")
time.sleep(0.4)

# 2. Simulate tracing the decay parameter across a 10-epoch training sequence
print("\n--- Epoch Optimization Step Tracking ---")
for epoch in range(1, 10):
    calculated_lr = scheduler.compute_epoch_lr(epoch)
    print(f" -> Epoch {epoch:02d} | Scheduled Learning Rate Matrix Set to: {calculated_lr:.5f}")
    time.sleep(0.1)

print("-" * 50)
print("[SUCCESS] Optimization step paths computed and validated.")

print("=================================================")