import torch

def generate_dummy_data(num_samples=1000):
    X = torch.rand(num_samples, 10)
    care = X[:, 0] * 0.8 + X[:, 1] * 0.2
    fairness = X[:, 2] * 0.7 + X[:, 3] * 0.3
    loyalty = X[:, 4]
    authority = X[:, 5]
    purity = X[:, 6] * 0.6 + X[:, 7] * 0.4
    Y = torch.stack([care, fairness, loyalty, authority, purity], dim=1)
    return X, Y
