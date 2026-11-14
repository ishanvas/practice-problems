"""06. K-means clustering - PyTorch (GPU-friendly)

Same algorithm as 05, written with torch so it runs on mps / cuda.

Rules: no torch.cdist. No .item() / .cpu() / Python loops over points inside the
main loop (the convergence check can use one .item() per iteration).
Everything should stay on X's device.

  pairwise_sq_dists(X, C) -> (N, k)
  kmeans(X, k, n_iters=100, tol=1e-6, init=None, generator=None) -> (C, labels, inertia)
     init=None: pick k distinct random rows of X (use torch.randperm with generator)
     inertia: 0-dim tensor

Hint for the update step without a loop over k:
  sums   = torch.zeros(k, D).index_add_(0, labels, X)
  counts = torch.bincount(labels, minlength=k)
"""

import torch

from testkit import close, run


def pairwise_sq_dists(X: torch.Tensor, C: torch.Tensor) -> torch.Tensor:
    # TODO: your code here
    raise NotImplementedError


def kmeans(X, k, n_iters=100, tol=1e-6, init=None, generator=None):
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

torch.manual_seed(0)
DEV = "mps" if torch.backends.mps.is_available() else "cpu"


def _blobs(n=100, centers=((0, 0), (8, 0), (0, 8), (8, 8)), std=0.6):
    X = torch.cat([torch.randn(n, 2) * std + torch.tensor(c, dtype=torch.float32) for c in centers])
    return X, torch.arange(len(centers)).repeat_interleave(n)


def _same_partition(a, b):
    pairs = set(zip(a.tolist(), b.tolist()))
    return len(pairs) == len(set(a.tolist())) == len(set(b.tolist()))


def test_dists():
    X, C = torch.randn(50, 6), torch.randn(5, 6)
    close(pairwise_sq_dists(X, C), torch.cdist(X, C) ** 2, atol=1e-4, what="dists")


def test_fixed_init():
    X = torch.tensor([[0.0], [1], [2], [10], [11], [12]])
    C, labels, inertia = kmeans(X, 2, init=torch.tensor([[0.0], [1.0]]))
    close(C.sort(0).values, [[1], [11]], what="centroids")
    close(inertia, 4.0, what="inertia")


def test_empty_cluster():
    X = torch.tensor([[0.0, 0], [1, 0], [0, 1]])
    C, labels, _ = kmeans(X, 2, init=torch.tensor([[0.3, 0.3], [100.0, 100.0]]))
    close(C[1], [100, 100], what="empty cluster centroid")
    assert torch.isfinite(C).all(), "nan centroid (divide by zero count?)"


def test_blobs_on_device():
    X, y = _blobs()
    X = X.to(DEV)
    best = None
    for s in range(5):  # random init can hit a local optimum; keep the best of 5
        g = torch.Generator().manual_seed(s)
        res = kmeans(X, 4, generator=g)
        if best is None or res[2] < best[2]:
            best = res
    C, labels, inertia = best
    assert C.device.type == DEV and labels.device.type == DEV, f"left {DEV}: {C.device}"
    assert inertia.dim() == 0, "inertia should be a 0-dim tensor"
    assert _same_partition(labels.cpu(), y), "didn't recover the 4 blobs"


if __name__ == "__main__":
    run(f"k-means (torch, device={DEV})", [
        (test_dists, "pairwise_sq_dists matches cdist^2"),
        (test_fixed_init, "converges from a given init"),
        (test_empty_cluster, "empty cluster keeps its centroid, no nan"),
        (test_blobs_on_device, "recovers 4 blobs and stays on device"),
    ])
