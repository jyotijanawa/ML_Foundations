import torch
import numpy as np
print("=============================================")
print("PYTORCH DEEP LEARNING ENGINE CORES CORE")
print("==========================================")
face_feature_tensor = torch.tensor([0.5,1.2,-0.8,2.0], dtype=torch.float32)
print(f"[INPUT] Layer Input Scan Tensor:\n{face_feature_tensor.numpy()}")
print("-"*50)
weights = torch.constant([
    [0.2,0.8,-0.5,1.0],
    [0.5,-0.1,0.9,0.4],
    [0.1,0.4,0.3,-0.7],
    [0.9,0.2,-0.2,0.5]
], dtype=torch.float32)
layer_signal = torch.matmul(tf.reshape(face_feature_tensor,(1,4)),weights)
print(f"Raw Signal Accumulation Layer Output:\n{layer_signal.numpy()}")
print("-"*50)
activated_output = torch.relu(layer_signal)
print("Final Activated Neuron Outputs (ReLU Applied):")
print(activated_output.numpy())
print("\n(Notice: Any negative signal from the previous step is now a perfect 0.0!)")
print("==================================================")