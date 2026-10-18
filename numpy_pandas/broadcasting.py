import numpy as np

x = np.random.rand(5, 3)
print(x)

def standardise(x):
    x_scaled = x.astype(float)
    for col in range(len(x_scaled[0])):
        col_mean = x_scaled[:,col].mean(axis=0)
        col_std = x_scaled[:,col].std(axis=0)
        for row in range(len(x_scaled)):
            x_scaled[row, col] -= col_mean
            x_scaled[row, col] /= col_std
    return x_scaled
print(standardise(x).mean(axis = 0))

def standardise_fast(x):
    x_scaled = x.astype(float)
    x_scaled -= x_scaled.mean(axis = 0)
    x_scaled /= x_scaled.std(axis = 0)
    return x_scaled

slow = standardise(x)
fast = standardise_fast(x)
print(fast.mean(axis=0))
print(fast.std(axis=0))
print(np.allclose(slow, fast))