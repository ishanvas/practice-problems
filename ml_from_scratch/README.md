# ML from scratch — NumPy & PyTorch practice

Each file has a problem description at the top, stubs marked `# TODO`, and tests
at the bottom. Fill in the stubs, then run the file:

```bash
cd ~/python-projects/ml_from_scratch
~/.venvs/ml/bin/python 01_attention_numpy.py
```

(The project's `.venv` has no numpy/torch, so use the shared `~/.venvs/ml` env.)

Most tests compare your output to PyTorch's own implementation
(`F.scaled_dot_product_attention`, `nn.MultiheadAttention`, `nn.TransformerEncoderLayer`, …).

| # | File | What you build |
|---|------|----------------|
| 01 | `01_attention_numpy.py` | stable softmax, causal mask, scaled dot-product attention |
| 02 | `02_attention_torch.py` | same in torch: autograd, devices (mps) |
| 03 | `03_multihead_attention_numpy.py` | split/merge heads, multi-head self- and cross-attention |
| 04 | `04_multihead_attention_torch.py` | `MultiHeadAttention` nn.Module |
| 05 | `05_kmeans_numpy.py` | vectorised distances, Lloyd's algorithm, k-means++ |
| 06 | `06_kmeans_torch.py` | k-means on GPU, no Python loops |
| 07 | `07_logistic_regression_numpy.py` | stable sigmoid/BCE, gradients by hand, gradient check, L2 |
| 08 | `08_logistic_regression_torch.py` | nn.Module + training loop with autograd and SGD |
| 09 | `09_transformer_block_torch.py` | pre-LN transformer block, sinusoidal positions (uses 04) |
| 10 | `10_tiny_transformer_lm.py` | GPT-style LM, next-token loss, training, greedy generation (uses 09) |

Mind the mask convention: in these files `True` means the query **may attend** to that key.
`nn.MultiheadAttention` uses the opposite (`True` = blocked); the tests handle the conversion for you.
