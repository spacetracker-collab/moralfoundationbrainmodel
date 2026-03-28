import torch
import torch.nn as nn

class MoralFoundationNet(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=32, output_dim=5):
        super(MoralFoundationNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)
