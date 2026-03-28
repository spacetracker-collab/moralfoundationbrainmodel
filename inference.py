import torch
from model import MoralFoundationNet

FOUNDATIONS = ["care", "fairness", "loyalty", "authority", "purity"]

def interpret_output(scores):
    decision = {}
    for i, f in enumerate(FOUNDATIONS):
        decision[f] = float(scores[i])

    if decision["care"] > 0.7 and decision["fairness"] > 0.7:
        recommendation = "APPROVE (ethical)"
    elif decision["authority"] > 0.7 and decision["loyalty"] > 0.6:
        recommendation = "APPROVE (institutional alignment)"
    elif decision["purity"] > 0.8:
        recommendation = "REJECT (ethical violation)"
    else:
        recommendation = "REVIEW REQUIRED"

    return decision, recommendation

def run_inference(sample_input):
    model = MoralFoundationNet()
    model.load_state_dict(torch.load("moral_model.pt"))
    model.eval()

    with torch.no_grad():
        input_tensor = torch.tensor(sample_input).float()
        output = model(input_tensor)

    return interpret_output(output)

if __name__ == "__main__":
    sample = [0.9, 0.8, 0.2, 0.3, 0.1, 0.4, 0.2, 0.1, 0.5, 0.6]
    decision, recommendation = run_inference(sample)
    print(decision)
    print(recommendation)
