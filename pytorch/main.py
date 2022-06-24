my_dict = {
    'region': ['Kanto', 'Johto', 'Hoenn', 'Sinnoh', 'Unova', 'Kalos'],
    'temperature': [38.5, 36.7, 35.4, 33.5, 31.9, 30.2],
    'rainfall': [1.5, 1.8, 2.5, 3.0, 3.8, 4.5],
    'humidity': [22.2, 20.0, 19.0, 17.2, 15.4, 14.0],
    'apple (ton)': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
    'orange (ton)': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
}

# in linear regression model each target variable as estimated to be weighted sum of the input variables, offset by some constant, know as bias

# yield_apple = w11 * my_dict['temperature'] + w12 * my_dict['rainfall'] + w13 * my_dict['humidity'] +  + b1

import numpy as np
import torch

# input: (temp, rainfall, humidity)
inputs = np.array([[73, 65, 70], [93, 85, 90], [89, 80, 75], [70, 65, 70], [80, 75, 80]], dtype='float32')

targets = np.array([[152, 185, 170], [185, 210, 195], [175, 200, 175], [150, 175, 160], [175, 200, 175]], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# weights and biases
w = torch.randn(2, 3, requires_grad=True)
b = torch.randn(2, requires_grad=True)

# model like function that performs a matrix multiplication of the inputs and the weights w (transpose) and adds the bias b
def model(x):
    return x @ w.t() + b # @ represents matrix multiplication

# generate prediction
preds = model(inputs)
print(preds)
print(targets) # compare with target

# mse loss
def mse(t1, t2):
    diff = t1 - t2
    return torch.sum(diff * diff) / diff.numel()

# compute loss
loss = mse(preds, targets)
print(loss)

# compute gradients
loss.backward()

# gradients for weights
print(w)
print(w.grad)

# gradient element is positive
    # increasing: the element's value slightly will increase the loss
    # decreasing: the element's value slightly will decrease the loss
# gradient element is negative
    # increasing: the element's value slightly will decrease the loss
    # decreasing: the element's value slightly will increase the loss

# reset the gradient to zero
w.grad.zero_()
b.grad.zero_()

# adjust weights and reset gradient
with torch.no_grad():
    w -= w.grad * 1e-5
    b -= b.grad * 1e-5
    w.grad.zero_()
    b.grad.zero_()

# calculate loss again
preds = model(inputs)
loss = mse(preds, targets)
print(loss)

# train for multiple epochs
for i in range(100):
    preds = model(inputs)
    loss = mse(preds, targets)
    loss.backward()
    with torch.no_grad():
        w -= w.grad * 1e-5
        b -= b.grad * 1e-5
        w.grad.zero_()
        b.grad.zero_()

# calculate loss again
preds = model(inputs)
loss = mse(preds, targets)
print(loss)
