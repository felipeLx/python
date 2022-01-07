import numpy as np
np.random.rand()

# pseudo random
np.random.seed(123)
# same seed, same random numbers
np.random.rand()
np.random.rand() # ensures reproducibility

# coin toss
np.random.seed(123)
coin = np.random.randint(0,2) # randomly generate 0 or 1
print(coin)
# how the seed is the same, the coin value always will be the same
if coin == 0:
    print("heads")
else:
    print("tails")

np.random.seed(300)
# Use randint() to simulate a dice
print(np.random.randint(1, 7))

step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2:
    step = step - 1
elif dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1,7)

np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)

tails = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)