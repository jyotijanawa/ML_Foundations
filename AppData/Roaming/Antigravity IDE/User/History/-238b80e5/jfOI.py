import tensorflow as tf 
import numpy as np
print("=============================================")
print("TENSORFLOW DEEP LEARNING ENGINE CORES CORE")
print("==========================================")
face_feature_tensor = tf.constant([0.5,1.2,-0.8,2.0], dtype=tf.float32)
print(f"[INPUT] Layer Input Scan Tensor:\n{face_feature_tensor.numpy()}")
print("-"*50)
weights = tf.constant([
    [0.2,0.8,-0.5,1.0],
    [0.5,-0.1,0.9,0.4],
    [0.1,0.4,0.3,-0.7],
    [0.9,0.2,-0.2,0.5]
], dtype=tf.float32)
layer_signal = tf.matmul(tf.reshape(face_feature_tensor,(1,4)),weights)
print(f"Raw Signal Accumulation Layer Output:\n{layer_signal.numpy()}")
print("-"*50)
activated_output = tf.nn.relu(layer_signal)
print("Final Activated Neuron Outputs (ReLU Applied):")
print(activated_output.numpy())
print("\n(Notice: Any negative signal from the previous step is now a perfect 0.0!)")
print("==================================================")