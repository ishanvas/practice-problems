"""10. Tiny decoder-only transformer language model - PyTorch

Stack your TransformerBlock from 09 into a GPT-style model and train it.

  TinyLM(vocab_size, d_model, n_heads, n_layers, max_len, d_ff=4*d_model)
    self.tok_emb : nn.Embedding(vocab_size, d_model)
    self.pos_emb : nn.Embedding(max_len, d_model)       (learned positions)
    self.blocks  : nn.ModuleList of n_layers TransformerBlock
    self.ln_f    : nn.LayerNorm(d_model)
    self.head    : nn.Linear(d_model, vocab_size, bias=False)

    forward(idx (B, L) long) -> logits (B, L, vocab_size)
        always causal: position t only sees tokens 0..t
    generate(idx (B, L), n_new) -> (B, L + n_new)
        greedy (argmax) decoding; crop the context to the last max_len tokens.
        Use torch.no_grad().

  lm_loss(logits, idx): next-token cross-entropy - predict idx[:, t+1] from logits[:, t].
        F.cross_entropy is fine here; mind the shift and the reshape.

The tests train on a toy task (each token = previous + 1 mod vocab) and expect
the model to learn it - if your blocks are subtly wrong, this is where it shows.
"""

import importlib

import torch
import torch.nn as nn
import torch.nn.functional as F

from testkit import close, run

TransformerBlock = importlib.import_module("09_transformer_block_torch").TransformerBlock


class TinyLM(nn.Module):

    def __init__(self, vocab_size, d_model, n_heads, n_layers, max_len, d_ff=None):
        super().__init__()
        d_ff = d_ff or 4 * d_model
        self.max_len = max_len
        # TODO: your code here
        raise NotImplementedError

    def forward(self, idx):
        # TODO: your code here
        raise NotImplementedError

    def generate(self, idx, n_new):
        # TODO: your code here
        raise NotImplementedError


def lm_loss(logits, idx):
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)
V = 12


def _batch(B=32, L=16):
    start = torch.randint(0, V, (B, 1))
    return (start + torch.arange(L)) % V


def test_shapes():
    m = TinyLM(V, 32, 4, 2, max_len=16)
    idx = torch.randint(0, V, (3, 10))
    assert m(idx).shape == (3, 10, V), f"logits shape {tuple(m(idx).shape)}"
    assert len(m.blocks) == 2 and isinstance(m.blocks[0], TransformerBlock)


def test_causal():
    m = TinyLM(V, 32, 4, 2, max_len=16)
    a = torch.randint(0, V, (1, 10))
    b = a.clone()
    b[0, 6:] = (b[0, 6:] + 1) % V
    close(m(a)[0, :6], m(b)[0, :6], what="logits before the change")


def test_lm_loss():
    logits = torch.randn(2, 5, V)
    idx = torch.randint(0, V, (2, 5))
    want = F.cross_entropy(logits[:, :4].transpose(1, 2), idx[:, 1:])
    close(lm_loss(logits, idx), want, what="loss")


def test_learns_and_generates():
    torch.manual_seed(0)
    m = TinyLM(V, 32, 4, 2, max_len=16)
    opt = torch.optim.AdamW(m.parameters(), lr=3e-3)
    for _ in range(200):
        idx = _batch()
        loss = lm_loss(m(idx), idx)
        opt.zero_grad()
        loss.backward()
        opt.step()
    assert loss.item() < 0.1, f"final loss {loss.item():.3f}, want < 0.1"
    out = m.generate(torch.tensor([[3, 4, 5]]), n_new=20)  # 23 > max_len: tests cropping
    want = (torch.arange(23) + 3) % V
    assert out.shape == (1, 23), f"shape {tuple(out.shape)}"
    assert out[0].tolist() == want.tolist(), f"generated {out[0].tolist()}"


if __name__ == "__main__":
    run("tiny transformer LM (torch)", [
        (test_shapes, "forward gives (B, L, vocab) logits"),
        (test_causal, "always causal"),
        (test_lm_loss, "lm_loss shifts targets by one"),
        (test_learns_and_generates, "learns 'next = prev + 1' and generates past max_len"),
    ])
