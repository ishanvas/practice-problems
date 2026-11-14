"""01. Scaled dot-product attention - NumPy

    Attention(Q, K, V) = softmax(Q @ K^T / sqrt(d_k)) @ V

Shapes (any number of leading batch dims "..." is allowed):
  Q: (..., Lq, d_k)   queries
  K: (..., Lk, d_k)   keys
  V: (..., Lk, d_v)   values
  -> out:     (..., Lq, d_v)
  -> weights: (..., Lq, Lk)   each row sums to 1

mask: optional boolean array broadcastable to (..., Lq, Lk).
      True = this query MAY attend to this key, False = blocked.
      (Same convention as torch.nn.functional.scaled_dot_product_attention.)
      Blocked scores should get -inf (or a very large negative) before softmax.

Rules: NumPy only, no Python loops over batch or sequence positions.

Things to get right:
  - numerically stable softmax (subtract the max before exp)
  - the 1/sqrt(d_k) scaling - why is it there?
  - matmul with batch dims: np.matmul / @ and swapaxes(-1, -2)
"""

import numpy as np

from testkit import close, run


def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    """Numerically stable softmax along axis."""
    num = np.exp(-x)
    deno = np.sum(num, axis=axis)
    print (f'okok {num/deno}')
    return num/deno
    


def causal_mask(L: int) -> np.ndarray:
    """(L, L) boolean mask: query i may attend to keys 0..i (lower triangle incl. diagonal)."""
    i = np.arange(L)[:, None]   # row (query) indices, shape (L, 1)
    j = np.arange(L)[None, :]   # column (key) indices, shape (1, L)
    return j <= i               # broadcasts to (L, L) bool: True where key j <= query i



def scaled_dot_product_attention(Q, K, V, mask=None):
    """Return (out, weights). See module docstring for shapes."""
    # TODO: your code here
    n, d = Q.shape
    weights = Q @ K.T/np.sqrt(d)
    masked_weights = weights @ causal_mask(n)
    cav = softmax(masked_weights) @ V
    return cav
    



# ----------------------------------------------------------------- tests ----

def _torch_ref(Q, K, V, mask=None):
    import torch
    import torch.nn.functional as F
    t = lambda a: torch.from_numpy(a)
    m = None if mask is None else torch.from_numpy(np.asarray(mask))
    return F.scaled_dot_product_attention(t(Q), t(K), t(V), attn_mask=m).numpy()


rng = np.random.default_rng(0)


def test_softmax_basic():
    x = rng.normal(size=(4, 7))
    s = softmax(x)
    close(s.sum(-1), np.ones(4), what="rows sum")
    close(s, np.exp(x) / np.exp(x).sum(-1, keepdims=True), what="softmax")


def test_softmax_stable():
    s = softmax(np.array([[1000.0, 1001.0, 1002.0]]))
    assert np.isfinite(s).all(), "got nan/inf - subtract the max first"
    close(s, softmax(np.array([[0.0, 1.0, 2.0]])), what="shift invariance")


def test_softmax_axis():
    x = rng.normal(size=(3, 5))
    close(softmax(x, axis=0).sum(0), np.ones(5), what="axis=0 sums")


def test_causal_mask():
    m = causal_mask(4)
    assert m.dtype == bool, f"dtype {m.dtype}, want bool"
    want = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]], bool)
    assert (m == want).all(), f"got\n{m.astype(int)}"


def test_uniform_keys():
    # identical keys -> every key gets the same score -> output = mean of V
    Q = rng.normal(size=(3, 4))
    K = np.ones((5, 4))
    V = rng.normal(size=(5, 2))
    out, w = scaled_dot_product_attention(Q, K, V)
    close(w, np.full((3, 5), 0.2), what="weights")
    close(out, np.tile(V.mean(0), (3, 1)), what="out")


def test_matches_torch():
    Q, K, V = rng.normal(size=(6, 8)), rng.normal(size=(9, 8)), rng.normal(size=(9, 3))
    out, w = scaled_dot_product_attention(Q, K, V)
    assert w.shape == (6, 9), f"weights shape {w.shape}, want (6, 9)"
    close(out, _torch_ref(Q, K, V), what="out")


def test_batched():
    Q, K, V = (rng.normal(size=(2, 3, 5, 4)) for _ in range(3))
    out, w = scaled_dot_product_attention(Q, K, V)
    close(out, _torch_ref(Q, K, V), what="out")
    close(w.sum(-1), np.ones((2, 3, 5)), what="weight rows sum")


def test_causal():
    L = 6
    Q, K, V = (rng.normal(size=(2, L, 4)) for _ in range(3))
    m = causal_mask(L)
    out, w = scaled_dot_product_attention(Q, K, V, mask=m)
    close(w[:, ~m], np.zeros((2, (~m).sum())), what="weights above diagonal")
    close(out, _torch_ref(Q, K, V, m), what="out")
    close(out[:, 0], V[:, 0], what="first position only sees itself")


if __name__ == "__main__":
    run("scaled dot-product attention (numpy)", [
        (test_softmax_basic, "softmax rows sum to 1 and match the formula"),
        (test_softmax_stable, "softmax doesn't overflow on large inputs"),
        (test_softmax_axis, "softmax respects axis"),
        (test_causal_mask, "causal_mask is lower triangular bool"),
        (test_uniform_keys, "identical keys -> uniform weights, mean of V"),
        (test_matches_torch, "matches torch, Lq != Lk, d_v != d_k"),
        (test_batched, "works with extra batch dims (B, H, L, d)"),
        (test_causal, "causal mask blocks the future"),
    ])
