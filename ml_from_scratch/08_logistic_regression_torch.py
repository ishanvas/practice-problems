"""08. Logistic regression - PyTorch, with autograd + a training loop

Now let autograd do the gradients, and practise the standard torch training loop:
    optimizer.zero_grad(); loss = ...; loss.backward(); optimizer.step()

  LogisticRegression(d)       nn.Module with self.linear = nn.Linear(d, 1)
      forward(X (N, d)) -> logits (N,)     (no sigmoid! return raw logits)
  bce_with_logits(logits, y)  mean BCE, stable for huge logits.
                              Write it yourself (no F.binary_cross_entropy*,
                              no nn.BCE*). Hint: F.softplus(z) = log(1 + e^z), stably.
  train(model, X, y, lr, epochs, weight_decay=0.0) -> list of loss floats per epoch
                              full-batch, torch.optim.SGD.
  accuracy(model, X, y)       float in [0, 1]; use torch.no_grad()
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from testkit import close, run


class LogisticRegression(nn.Module):

    def __init__(self, d: int):
        super().__init__()
        # TODO: your code here
        raise NotImplementedError

    def forward(self, X):
        # TODO: your code here
        raise NotImplementedError


def bce_with_logits(logits, y):
    # TODO: your code here
    raise NotImplementedError


def train(model, X, y, lr=0.1, epochs=200, weight_decay=0.0):
    # TODO: your code here
    raise NotImplementedError


def accuracy(model, X, y):
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)


def _data(n=400, d=4):
    X = torch.randn(n, d)
    w = torch.randn(d) * 3
    y = (X @ w - 0.5 + 0.5 * torch.randn(n) > 0).float()
    return X, y


def test_forward_shape():
    m = LogisticRegression(5)
    out = m(torch.randn(7, 5))
    assert out.shape == (7,), f"shape {tuple(out.shape)}, want (7,) - squeeze the last dim"
    assert sum(p.numel() for p in m.parameters()) == 6, "should be one nn.Linear(d, 1)"


def test_bce():
    z, y = torch.randn(20) * 3, (torch.rand(20) > 0.5).float()
    close(bce_with_logits(z, y), F.binary_cross_entropy_with_logits(z, y), what="loss")
    big = bce_with_logits(torch.tensor([1000.0, -1000.0]), torch.tensor([0.0, 1.0]))
    close(big, 1000.0, what="loss at huge logits (finite?)")


def test_bce_grad():
    z = (torch.randn(10, dtype=torch.float64) * 2).requires_grad_()
    y = (torch.rand(10) > 0.5).double()
    bce_with_logits(z, y).backward()
    close(z.grad, (torch.sigmoid(z) - y) / 10, what="dL/dz")


def test_train():
    X, y = _data()
    m = LogisticRegression(4)
    losses = train(m, X, y, lr=0.5, epochs=300)
    assert isinstance(losses, list) and len(losses) == 300, "return one float per epoch"
    assert losses[-1] < losses[0] * 0.5, f"loss {losses[0]:.3f} -> {losses[-1]:.3f}"
    acc = accuracy(m, X, y)
    assert acc > 0.9, f"accuracy {acc:.2f}"


def test_weight_decay():
    X, y = _data()
    torch.manual_seed(1); a = LogisticRegression(4)
    torch.manual_seed(1); b = LogisticRegression(4)
    train(a, X, y, lr=0.5, epochs=200)
    train(b, X, y, lr=0.5, epochs=200, weight_decay=0.3)
    assert b.linear.weight.norm() < a.linear.weight.norm(), "weight_decay should shrink weights"


if __name__ == "__main__":
    run("logistic regression (torch)", [
        (test_forward_shape, "forward returns (N,) logits from one Linear"),
        (test_bce, "bce_with_logits matches torch and is stable"),
        (test_bce_grad, "autograd gives dL/dz = (sigmoid(z) - y) / N"),
        (test_train, "training loop reduces loss, > 90% accuracy"),
        (test_weight_decay, "weight_decay shrinks the weights"),
    ])
