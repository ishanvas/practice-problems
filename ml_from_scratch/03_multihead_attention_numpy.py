"""03. Multi-head attention - NumPy

  MultiHead(x_q, x_kv) = concat(head_1..head_H) @ Wo + bo
  head_h = Attention(Q_h, K_h, V_h)
  Q = x_q @ Wq + bq,  K = x_kv @ Wk + bk,  V = x_kv @ Wv + bv   (all D -> D)

Each of Q, K, V is (B, L, D). Split the last dim into H heads of size
d_head = D // H: head h owns columns h*d_head : (h+1)*d_head.

Shapes:
  x_q:  (B, Lq, D)    x_kv: (B, Lk, D)   (self-attention: x_q is x_kv)
  W*:   (D, D)        b*:   (D,)         (y = x @ W + b)
  mask: optional bool, broadcastable to (B, H, Lq, Lk), True = may attend
  -> out (B, Lq, D), weights (B, H, Lq, Lk)

Rules: NumPy only, no loops over heads - use reshape + transpose.

Write split_heads / merge_heads first; they're the part people get wrong
(reshape to (B, L, H, d_head) THEN transpose; not reshape straight to (B, H, L, d_head)).
"""

import numpy as np

from testkit import close, run


def softmax(x, axis=-1):
    # TODO: your code here
    raise NotImplementedError


def split_heads(x: np.ndarray, n_heads: int) -> np.ndarray:
    """(B, L, D) -> (B, H, L, D // H)"""
    # TODO: your code here
    raise NotImplementedError


def merge_heads(x: np.ndarray) -> np.ndarray:
    """(B, H, L, d_head) -> (B, L, H * d_head). Inverse of split_heads."""
    # TODO: your code here
    raise NotImplementedError


def multi_head_attention(x_q, x_kv, Wq, bq, Wk, bk, Wv, bv, Wo, bo, n_heads, mask=None):
    """Return (out, weights). See module docstring."""
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

rng = np.random.default_rng(0)


def _params(D):
    return [rng.normal(size=s) * 0.5 for s in [(D, D), (D,)] * 4]


def _torch_ref(x_q, x_kv, params, H, mask=None):
    """Same computation with torch.nn.MultiheadAttention as the oracle."""
    import torch
    D = x_q.shape[-1]
    Wq, bq, Wk, bk, Wv, bv, Wo, bo = [torch.from_numpy(p) for p in params]
    mha = torch.nn.MultiheadAttention(D, H, batch_first=True, dtype=torch.float64)
    with torch.no_grad():  # torch stores weights as (out, in): y = x @ W.T + b
        mha.in_proj_weight.copy_(torch.cat([Wq.T, Wk.T, Wv.T]))
        mha.in_proj_bias.copy_(torch.cat([bq, bk, bv]))
        mha.out_proj.weight.copy_(Wo.T)
        mha.out_proj.bias.copy_(bo)
    m = None if mask is None else ~torch.from_numpy(mask)  # torch: True = BLOCKED
    out, w = mha(torch.from_numpy(x_q), torch.from_numpy(x_kv), torch.from_numpy(x_kv),
                 attn_mask=m, average_attn_weights=False)
    return out.detach().numpy(), w.detach().numpy()


def test_split_heads():
    x = np.arange(2 * 3 * 6).reshape(2, 3, 6)
    s = split_heads(x, 2)
    assert s.shape == (2, 2, 3, 3), f"shape {s.shape}, want (2, 2, 3, 3)"
    assert (s[1, 0, 2] == x[1, 2, 0:3]).all(), "head 0 should own columns 0:3"
    assert (s[1, 1, 2] == x[1, 2, 3:6]).all(), "head 1 should own columns 3:6"


def test_merge_roundtrip():
    x = rng.normal(size=(2, 5, 12))
    close(merge_heads(split_heads(x, 4)), x, what="merge(split(x))")


def test_self_attention():
    D, H = 16, 4
    x = rng.normal(size=(2, 5, D))
    p = _params(D)
    out, w = multi_head_attention(x, x, *p, n_heads=H)
    ref_out, ref_w = _torch_ref(x, x, p, H)
    close(w, ref_w, what="weights")
    close(out, ref_out, what="out")


def test_cross_attention():
    D, H = 12, 3
    xq, xkv = rng.normal(size=(2, 4, D)), rng.normal(size=(2, 7, D))
    p = _params(D)
    out, w = multi_head_attention(xq, xkv, *p, n_heads=H)
    assert w.shape == (2, H, 4, 7), f"weights shape {w.shape}"
    close(out, _torch_ref(xq, xkv, p, H)[0], what="out")


def test_causal():
    D, H, L = 8, 2, 5
    x = rng.normal(size=(3, L, D))
    p = _params(D)
    m = np.tril(np.ones((L, L), bool))
    out, _ = multi_head_attention(x, x, *p, n_heads=H, mask=m)
    close(out, _torch_ref(x, x, p, H, m)[0], what="out")


def test_one_head_is_plain_attention():
    D = 6
    x = rng.normal(size=(1, 4, D))
    Wq, bq, Wk, bk, Wv, bv, Wo, bo = _params(D)
    out, _ = multi_head_attention(x, x, Wq, bq, Wk, bk, Wv, bv, Wo, bo, n_heads=1)
    Q, K, V = x @ Wq + bq, x @ Wk + bk, x @ Wv + bv
    w = softmax(Q @ K.swapaxes(-1, -2) / np.sqrt(D))
    close(out, (w @ V) @ Wo + bo, what="out")


if __name__ == "__main__":
    run("multi-head attention (numpy)", [
        (test_split_heads, "split_heads gives each head its own columns"),
        (test_merge_roundtrip, "merge_heads undoes split_heads"),
        (test_one_head_is_plain_attention, "n_heads=1 is plain attention + projections"),
        (test_self_attention, "self-attention matches nn.MultiheadAttention"),
        (test_cross_attention, "cross-attention (Lq != Lk)"),
        (test_causal, "causal mask"),
    ])
