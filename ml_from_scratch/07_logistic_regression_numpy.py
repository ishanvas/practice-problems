"""07. Logistic regression - NumPy, gradients by hand

Model:   z = X @ w + b,  p = sigmoid(z) = P(y=1 | x)
Loss:    mean binary cross-entropy + L2 on w (not b)
         L = mean( -y log p - (1-y) log(1-p) ) + (l2 / 2) * ||w||^2

Shapes: X (N, D), y (N,) of 0/1, w (D,), b scalar float.

Write the loss in terms of the logits z, not p, so it never takes log(0):
    -y log p - (1-y) log(1-p)  ==  log(1 + e^z) - y z    (= np.logaddexp(0, z) - y*z)
Derive the gradient yourself (it's short!) - dL/dz has a famous simple form.

sigmoid must not overflow for z = -1000 (np.exp(1000) = inf -> warnings / nan).
fit: full-batch gradient descent from w = 0, b = 0.
"""

import numpy as np

from testkit import close, run


def sigmoid(z: np.ndarray) -> np.ndarray:
    # TODO: your code here
    raise NotImplementedError


def loss_and_grad(w, b, X, y, l2=0.0):
    """Return (loss, dw, db)."""
    # TODO: your code here
    raise NotImplementedError


def fit(X, y, lr=0.1, epochs=1000, l2=0.0):
    """Gradient descent. Return (w, b)."""
    # TODO: your code here
    raise NotImplementedError


def predict_proba(w, b, X):
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

rng = np.random.default_rng(0)


def _data(n=200, d=3):
    X = rng.normal(size=(n, d))
    w_true = rng.normal(size=d) * 3
    y = (X @ w_true + 0.5 + rng.normal(size=n) * 0.5 > 0).astype(float)
    return X, y


def test_sigmoid():
    z = np.array([-3.0, 0.0, 2.0])
    close(sigmoid(z), 1 / (1 + np.exp(-z)), what="sigmoid")
    with np.errstate(over="raise", invalid="raise"):
        s = sigmoid(np.array([-1000.0, 1000.0]))
    close(s, [0, 1], what="extremes")


def test_loss_value():
    import torch
    X, y = _data(50)
    w, b = rng.normal(size=3), 0.3
    loss, _, _ = loss_and_grad(w, b, X, y, l2=0.0)
    ref = torch.nn.functional.binary_cross_entropy_with_logits(
        torch.from_numpy(X @ w + b), torch.from_numpy(y))
    close(loss, ref.item(), what="loss")


def test_loss_extreme():
    X = np.array([[1.0]])
    loss, dw, db = loss_and_grad(np.array([1000.0]), 0.0, X, np.array([0.0]))
    assert np.isfinite(loss) and np.isfinite(dw).all(), f"loss={loss}, dw={dw}"
    close(loss, 1000.0, what="loss for a confidently wrong prediction")


def test_gradient_check():
    X, y = _data(30, 4)
    w, b, l2, eps = rng.normal(size=4), -0.2, 0.1, 1e-6
    _, dw, db = loss_and_grad(w, b, X, y, l2)
    num_dw = np.zeros_like(w)
    for i in range(len(w)):
        e = np.zeros_like(w); e[i] = eps
        num_dw[i] = (loss_and_grad(w + e, b, X, y, l2)[0] - loss_and_grad(w - e, b, X, y, l2)[0]) / (2 * eps)
    num_db = (loss_and_grad(w, b + eps, X, y, l2)[0] - loss_and_grad(w, b - eps, X, y, l2)[0]) / (2 * eps)
    close(dw, num_dw, atol=1e-6, what="dw vs finite differences")
    close(db, num_db, atol=1e-6, what="db vs finite differences")


def test_fit():
    X, y = _data(400)
    w, b = fit(X, y, lr=0.5, epochs=500)
    acc = ((predict_proba(w, b, X) > 0.5) == y).mean()
    assert acc > 0.9, f"train accuracy {acc:.2f}, want > 0.9"


def test_l2_shrinks():
    X, y = _data(200)
    w0, _ = fit(X, y, lr=0.5, epochs=300, l2=0.0)
    w1, _ = fit(X, y, lr=0.5, epochs=300, l2=0.5)
    assert np.linalg.norm(w1) < np.linalg.norm(w0), "L2 should shrink the weights"


if __name__ == "__main__":
    run("logistic regression (numpy)", [
        (test_sigmoid, "sigmoid is correct and doesn't overflow"),
        (test_loss_value, "loss matches torch BCE-with-logits"),
        (test_loss_extreme, "loss stays finite for huge logits"),
        (test_gradient_check, "gradients match finite differences (with L2)"),
        (test_fit, "fit gets > 90% train accuracy"),
        (test_l2_shrinks, "L2 shrinks ||w||"),
    ])
