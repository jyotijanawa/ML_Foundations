
import numpy as np
print("=============================================")
print("NUMPY DEEP LEARNING ENGINE CORES CORE")
print("==========================================")
face_feature_tensor = np.array([0.5,1.2,-0.8,2.0], dtype=np.float32)
print(f"[INPUT] Layer Input Scan Vector:\n{face_feature_tensor}")
print("-"*50)
weights = np.array([
    [0.2,0.8,-0.5,1.0],
    [0.5,-0.1,0.9,0.4],
    [0.1,0.4,0.3,-0.7],
    [0.9,0.2,-0.2,0.5]
], dtype=np.float32)
layer_signal = np.dot(face_feature_tensor,weights)
print(f"Raw Signal Accumulation Layer Output:\n{layer_signal}")
print("-"*50)
activated_output = np.maximum(0,layer_signal)
print("Final Activated Neuron Outputs (ReLU Applied):")
print(activated_output)
print("\n(Notice: Any negative signal from the previous step is now a perfect 0.0!)")
print("==================================================")