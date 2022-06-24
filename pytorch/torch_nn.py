import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

# input (temp, rainfall, humidity)
inputs = np.array([[73, 65, 70], [93, 85, 90], [89, 80, 75], 
                   [70, 65, 70], [80, 75, 80], [91,88,64],
                   [87,134,58], [102,43,37], [69,96,70],
                   [70, 60, 65], [80, 80, 70], [88,74,60],
                   [87,120,58], [94,53,47], [65,90,70]], dtype='float32')

# targets (apple, orange)
targets = np.array([[56,70], [81,101], [119,113], 
                    [22,37], [103, 109], [56, 70],
                    [81,101], [119,133], [22, 37], 
                    [103, 109], [56, 70],[81,101],
                    [56,70], [81,101], [119,113]], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

# define dataset
train_ds = TensorDataset(inputs, targets)
train_ds[0:3] # create a tuple

# create dataloader - split the data into batches of a predefined size
batch_size = 5
train_dl = DataLoader(train_ds, batch_size, shuffle=True)

for xb, yb in train_dl:
    print('data loader: ', xb.shape, yb.shape)
    break

# define model by Linear
model = nn.Linear(3, 2)
print('model weight: ', model.weight)
print('model bias: ', model.bias)

# parameters
list(model.parameters())

# generate prediction
preds = model(inputs)
print('prediction: ', preds)

# loss function
import torch.nn.functional as F

loss_fn = F.mse_loss

loss = loss_fn(model(inputs), targets)
print('loss: ', loss)

# optimizer: SGD - stochastic gradient descent
opt = torch.optim.SGD(model.parameters(), lr=1e-5)

# train model
    # generate prediction  / calculate loss / compute gradiend / adjust the weights / reset the gradients
def fit(num_epochs, model, loss_fn, opt):
    for epoch in range(num_epochs):
        for xb, yb in train_dl:
            pred = model(xb)
            loss = loss_fn(pred, yb)
            loss.backward()
            opt.step()
            opt.zero_grad()
        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {}'.format(epoch+1, num_epochs, loss.item()))

# train model
fit(100, model, loss_fn, opt)

# generate prediction
preds = model(inputs)
print('prediction: ', preds)
print('targets: ', targets)