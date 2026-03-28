import torch
import torch.optim as optim
import torch.nn as nn
from model import MoralFoundationNet
from data import generate_dummy_data

def train():
    model = MoralFoundationNet()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.MSELoss()

    X, Y = generate_dummy_data()

    for epoch in range(50):
        optimizer.zero_grad()
        outputs = model(X)
        loss = loss_fn(outputs, Y)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item()}")

    torch.save(model.state_dict(), "moral_model.pt")
    print("Model saved.")

if __name__ == "__main__":
    train()
