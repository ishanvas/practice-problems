"""04. Multi-head attention - PyTorch nn.Module

Build MultiHeadAttention as an nn.Module. 09 (transformer block) imports it,
so finish this one first.

Required attribute names (the tests load weights into them):
  self.W_q, self.W_k, self.W_v, self.W_o : nn.Linear(d_model, d_model, bias=bias)
  self.n_heads, self.d_head

forward(q, k, v, mask=None) -> (out, weights)
  q: (B, Lq, D), k / v: (B, Lk, D)
  mask: optional bool broadcastable to (B, H, Lq, Lk), True = may attend
  out: (B, Lq, D), weights: (B, H, Lq, Lk)

Rules: no nn.MultiheadAttention / F.scaled_dot_product_attention.
torch.softmax is fine now (you wrote it yourself in 02).

Hints: .view(B, L, H, d_head).transpose(1, 2) to split heads;
.transpose(1, 2).contiguous().view(B, L, D) to merge (why is contiguous() needed?).
"""

import math

import torch
import torch.nn as nn

from testkit import close, run


class MultiHeadAttention(nn.Module):

    def __init__(self, d_model: int, n_heads: int, bias: bool = True):
        super().__init__()
        assert d_model % n_heads == 0, "d_model must be divisible by n_heads"
        # TODO: your code here
        raise NotImplementedError

    def forward(self, q, k, v, mask=None):
        # TODO: your code here
        raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)


def _pair(D, H, bias=True):
    """(mine, torch reference) with identical weights."""
    mine = MultiHeadAttention(D, H, bias=bias)
    ref = nn.MultiheadAttention(D, H, bias=bias, batch_first=True)
    with torch.no_grad():
        ref.in_proj_weight.copy_(torch.cat([mine.W_q.weight, mine.W_k.weight, mine.W_v.weight]))
        ref.out_proj.weight.copy_(mine.W_o.weight)
        if bias:
            ref.in_proj_bias.copy_(torch.cat([mine.W_q.bias, mine.W_k.bias, mine.W_v.bias]))
            ref.out_proj.bias.copy_(mine.W_o.bias)
    return mine, ref


def test_attributes():
    m = MultiHeadAttention(32, 4)
    assert m.n_heads == 4 and m.d_head == 8, f"n_heads={m.n_heads}, d_head={m.d_head}"
    for name in ("W_q", "W_k", "W_v", "W_o"):
        lin = getattr(m, name)
        assert isinstance(lin, nn.Linear) and lin.weight.shape == (32, 32), name
    n = sum(p.numel() for p in m.parameters())
    assert n == 4 * (32 * 32 + 32), f"{n} params, want {4 * (32 * 32 + 32)}"


def test_self_attention():
    mine, ref = _pair(32, 4)
    x = torch.randn(2, 6, 32)
    out, w = mine(x, x, x)
    ref_out, ref_w = ref(x, x, x, average_attn_weights=False)
    close(w, ref_w, what="weights")
    close(out, ref_out, what="out")


def test_cross_attention_no_bias():
    mine, ref = _pair(24, 3, bias=False)
    q, kv = torch.randn(2, 4, 24), torch.randn(2, 9, 24)
    close(mine(q, kv, kv)[0], ref(q, kv, kv)[0], what="out")


def test_causal():
    mine, ref = _pair(16, 2)
    x = torch.randn(3, 7, 16)
    m = torch.ones(7, 7, dtype=torch.bool).tril()
    out, w = mine(x, x, x, mask=m)
    close(out, ref(x, x, x, attn_mask=~m)[0], what="out")  # torch: True = BLOCKED
    assert (w[..., ~m] == 0).all(), "attending to the future"


def test_backward():
    mine, _ = _pair(16, 4)
    x = torch.randn(2, 5, 16, requires_grad=True)
    mine(x, x, x)[0].sum().backward()
    assert x.grad is not None and torch.isfinite(x.grad).all(), "no/bad grad for input"
    for name, p in mine.named_parameters():
        assert p.grad is not None, f"no grad for {name}"


if __name__ == "__main__":
    run("multi-head attention (torch nn.Module)", [
        (test_attributes, "layers named W_q/W_k/W_v/W_o, right param count"),
        (test_self_attention, "self-attention matches nn.MultiheadAttention"),
        (test_cross_attention_no_bias, "cross-attention, bias=False"),
        (test_causal, "causal mask"),
        (test_backward, "backward reaches input and every parameter"),
    ])
