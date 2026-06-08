import numpy as np 
print("=== Starting Advance Data Analytics Pipeline ===")
data_readings = np.array([48,52,50,350,49,53,400,51,47,50])
data_mean = np.mean(data_readings)
data_std = np.std(data_readings)
print(f"Total readings Collected: {len(data_readings)}")
print(f"Calculated Mean (Average): {data_mean:.2f} ms")
print(f"Standard Deviation (Volatily): {data_std:.2f} ms")
print("-" * 45)
threshold = data_mean + (1.5 * data_std)
print(f"Anomalous Outlier Threshold Set At: >{threshold:.2f} ms")
print("-" * 45)
print("Analyzing Stream for anomalies...")
for index, reading in enumerate(data_readings):
    if reading > threshold:
        print(f"Alert: Reading #{index} is an OUTLIER! Value: {reading}ms (System Spike)")
    else:
        print(f"Reading #{index}: {reading}ms - Normal Operation")
print("================================================")
