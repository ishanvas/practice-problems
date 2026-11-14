"""02. Scaled dot-product attention - PyTorch

Same as 01, now in PyTorch:

    Attention(Q, K, V) = softmax(Q @ K^T / sqrt(d_k)) @ V

  Q: (..., Lq, d_k), K: (..., Lk, d_k), V: (..., Lk, d_v)
  mask: optional bool tensor broadcastable to (..., Lq, Lk), True = may attend.
  -> (out (..., Lq, d_v), weights (..., Lq, Lk))

Rules: write softmax yourself (no torch.softmax / F.softmax / F.scaled_dot_product_attention).
It must be differentiable (autograd) and work on any device (cpu / mps).

Things to get right:
  - K.transpose(-2, -1) for batched transpose
  - masked_fill with float("-inf")
  - keep everything on the input's device / dtype (don't create CPU tensors by accident)
"""

import math

import torch
import torch.nn.functional as F

from testkit import close, run


def softmax(x: torch.Tensor, dim: int = -1) -> torch.Tensor:
    """Numerically stable softmax along dim."""
    # TODO: your code here
    raise NotImplementedError


def causal_mask(L: int, device=None) -> torch.Tensor:
    """(L, L) bool mask, True on and below the diagonal."""
    # TODO: your code here
    raise NotImplementedError


def scaled_dot_product_attention(Q, K, V, mask=None):
    """Return (out, weights)."""
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)


def test_softmax():
    x = torch.randn(4, 7)
    close(softmax(x), F.softmax(x, -1), what="softmax")
    close(softmax(x, dim=0), F.softmax(x, 0), what="softmax dim=0")
    big = torch.tensor([[1000.0, 1001.0, 1002.0]])
    assert torch.isfinite(softmax(big)).all(), "nan/inf on large inputs"


def test_causal_mask():
    m = causal_mask(3)
    assert m.dtype == torch.bool, f"dtype {m.dtype}"
    assert m.tolist() == [[True, False, False], [True, True, False], [True, True, True]], m


def test_matches_torch():
    Q, K, V = torch.randn(2, 4, 5, 8), torch.randn(2, 4, 7, 8), torch.randn(2, 4, 7, 3)
    out, w = scaled_dot_product_attention(Q, K, V)
    assert w.shape == (2, 4, 5, 7), f"weights shape {tuple(w.shape)}"
    close(out, F.scaled_dot_product_attention(Q, K, V), what="out")


def test_causal():
    Q, K, V = (torch.randn(3, 6, 4) for _ in range(3))
    m = causal_mask(6)
    out, w = scaled_dot_product_attention(Q, K, V, m)
    close(out, F.scaled_dot_product_attention(Q, K, V, attn_mask=m), what="out")
    assert (w[:, ~m] == 0).all(), "attending to future positions"


def test_gradients():
    Q, K, V = (torch.randn(2, 5, 4, dtype=torch.float64, requires_grad=True) for _ in range(3))
    out, _ = scaled_dot_product_attention(Q, K, V, causal_mask(5))
    out.square().sum().backward()
    mine = [t.grad.clone() for t in (Q, K, V)]
    for t in (Q, K, V):
        t.grad = None
    ref = F.scaled_dot_product_attention(Q, K, V, attn_mask=causal_mask(5))
    ref.square().sum().backward()
    for name, g, t in zip("QKV", mine, (Q, K, V)):
        close(g, t.grad, what=f"grad {name}")


def test_device_dtype():
    dev = "mps" if torch.backends.mps.is_available() else "cpu"
    Q = torch.randn(2, 5, 4, device=dev, dtype=torch.float16 if dev == "mps" else torch.float64)
    out, w = scaled_dot_product_attention(Q, Q, Q, causal_mask(5, device=dev))
    assert out.device.type == dev and out.dtype == Q.dtype, f"got {out.device}/{out.dtype}"
    assert torch.isfinite(out).all(), "nan/inf"


if __name__ == "__main__":
    run("scaled dot-product attention (torch)", [
        (test_softmax, "softmax matches F.softmax and is stable"),
        (test_causal_mask, "causal_mask"),
        (test_matches_torch, "matches F.scaled_dot_product_attention (batched)"),
        (test_causal, "causal masking"),
        (test_gradients, "gradients match torch's"),
        (test_device_dtype, "stays on input device/dtype (mps fp16 if available)"),
    ])
