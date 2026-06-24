import numpy as np

np.random.seed(42)

x = np.random.rand(100, 1) * 10
y = 3 * x + 5 + np.random.randn(100, 1)

x_mean = np.mean(x)
x_std = np.std(x)

x = (x - x_mean) / x_std

w = np.random.randn(1)
b = np.random.randn(1)

learning_rate = 0.01
epochs = 1000

for epoch in range(epochs):
    y_pred = w * x + b

    dw = (-2 / len(x)) * np.sum(x * (y - y_pred))
    db = (-2 / len(x)) * np.sum(y - y_pred)

    w -= learning_rate * dw
    b -= learning_rate * db

loss = np.mean((y - y_pred) ** 2)

print("Weight:", w[0])
print("Bias:", b[0])
print("Final Loss:", loss)

test_x = np.array([[2.5]])
test_x = (test_x - x_mean) / x_std

prediction = w * test_x + b

print("Prediction for x=2.5:", prediction[0][0])