"""
Simple tests for learning models
"""
import torch


def load_models():
    poke_model = torch.load("poke_10k.pt")
    pushnet = torch.load("pushnet.pt")
    push_model = torch.load("push_forward_model.pkl")


def main():
    pass


if __name__ == "__main__":
    main()
