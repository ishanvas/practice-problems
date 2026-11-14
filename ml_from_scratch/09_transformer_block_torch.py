"""09. Transformer block (pre-LayerNorm, GPT-style) - PyTorch

Needs your MultiHeadAttention from 04 (imported below), so do 04 first.

  x = x + attn(ln1(x), mask)      # attention sub-layer + residual
  x = x + ff(ln2(x))              # feed-forward sub-layer + residual
  ff(x) = ff2(GELU(ff1(x)))       # D -> d_ff -> D

Required attribute names (the tests load weights into them):
  self.ln1, self.ln2 : nn.LayerNorm(d_model)
  self.attn          : MultiHeadAttention(d_model, n_heads)   (from 04)
  self.ff1           : nn.Linear(d_model, d_ff)
  self.ff2           : nn.Linear(d_ff, d_model)
  self.act           : nn.GELU()
  dropout: skip it (or add nn.Dropout and keep p=0 in the tests).

forward(x (B, L, D), mask=None) -> (B, L, D)

Also: sinusoidal_positional_encoding(L, D) -> (L, D) tensor  ("Attention Is All You Need")
  PE[pos, 2i]   = sin(pos / 10000^(2i / D))
  PE[pos, 2i+1] = cos(pos / 10000^(2i / D))
Vectorise it (no loops). Assume D is even.

Then in 10 you stack these blocks into a small language model.
"""

import importlib
import math

import torch
import torch.nn as nn

from testkit import close, run

MultiHeadAttention = importlib.import_module("04_multihead_attention_torch").MultiHeadAttention


class TransformerBlock(nn.Module):

    def __init__(self, d_model: int, n_heads: int, d_ff: int):
        super().__init__()
        # TODO: your code here
        raise NotImplementedError

    def forward(self, x, mask=None):
        # TODO: your code here
        raise NotImplementedError


def sinusoidal_positional_encoding(L: int, D: int) -> torch.Tensor:
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)


def _pair(D=32, H=4, F=64):
    mine = TransformerBlock(D, H, F)
    ref = nn.TransformerEncoderLayer(D, H, F, dropout=0.0, activation="gelu",
                                     batch_first=True, norm_first=True)
    for p in mine.parameters():  # random LN params too, so a swapped ln1/ln2 shows up
        nn.init.normal_(p, std=0.3)
    a = mine.attn
    with torch.no_grad():
        ref.self_attn.in_proj_weight.copy_(torch.cat([a.W_q.weight, a.W_k.weight, a.W_v.weight]))
        ref.self_attn.in_proj_bias.copy_(torch.cat([a.W_q.bias, a.W_k.bias, a.W_v.bias]))
        ref.self_attn.out_proj.weight.copy_(a.W_o.weight)
        ref.self_attn.out_proj.bias.copy_(a.W_o.bias)
        for r, m in [(ref.linear1, mine.ff1), (ref.linear2, mine.ff2),
                     (ref.norm1, mine.ln1), (ref.norm2, mine.ln2)]:
            r.weight.copy_(m.weight)
            r.bias.copy_(m.bias)
    return mine, ref


def test_shape_and_params():
    b = TransformerBlock(32, 4, 64)
    x = torch.randn(2, 5, 32)
    assert b(x).shape == x.shape, f"shape {tuple(b(x).shape)}"
    n = sum(p.numel() for p in b.parameters())
    want = 4 * (32 * 32 + 32) + 2 * 64 + (32 * 64 + 64) + (64 * 32 + 32)
    assert n == want, f"{n} params, want {want}"


def test_matches_torch():
    mine, ref = _pair()
    x = torch.randn(2, 6, 32)
    close(mine(x), ref(x), atol=1e-4, what="out")


def test_matches_torch_causal():
    mine, ref = _pair()
    x = torch.randn(3, 7, 32)
    m = torch.ones(7, 7, dtype=torch.bool).tril()
    close(mine(x, m), ref(x, src_mask=~m), atol=1e-4, what="out")  # torch: True = BLOCKED


def test_causal_no_leak():
    b = TransformerBlock(16, 2, 32)
    x = torch.randn(1, 6, 16)
    m = torch.ones(6, 6, dtype=torch.bool).tril()
    x2 = x.clone()
    x2[0, 4:] = torch.randn(2, 16)  # change the future
    close(b(x, m)[0, :4], b(x2, m)[0, :4], what="positions 0..3 after changing 4..5")


def test_positional_encoding():
    pe = sinusoidal_positional_encoding(50, 16)
    assert pe.shape == (50, 16), f"shape {tuple(pe.shape)}"
    close(pe[0], torch.tensor([0.0, 1.0] * 8), what="PE[0]")
    close(pe[1, :2], [math.sin(1), math.cos(1)], what="PE[1, :2]")
    close(pe[7, 2:4], [math.sin(7 / 10000 ** (2 / 16)), math.cos(7 / 10000 ** (2 / 16))],
          what="PE[7, 2:4]")


if __name__ == "__main__":
    run("transformer block (torch)", [
        (test_shape_and_params, "keeps shape, right number of params"),
        (test_matches_torch, "matches nn.TransformerEncoderLayer(norm_first=True)"),
        (test_matches_torch_causal, "matches torch with a causal mask"),
        (test_causal_no_leak, "future tokens don't affect the past"),
        (test_positional_encoding, "sinusoidal positional encoding"),
    ])
