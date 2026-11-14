"""05. K-means clustering - NumPy

Lloyd's algorithm:
  1. init k centroids
  2. assign: each point -> nearest centroid (squared Euclidean)
  3. update: each centroid -> mean of its points
     (empty cluster: keep its old centroid)
  4. repeat until centroids move less than tol (max |new - old|) or n_iters is hit

Shapes: X (N, D), C (k, D), labels (N,) ints in [0, k)
inertia = sum of squared distances from each point to its assigned centroid.

Rules: NumPy only. pairwise_sq_dists must be fully vectorised - use
    ||x - c||^2 = ||x||^2 - 2 x.c + ||c||^2
(no loops, and no (N, k, D) intermediate - think about why that matters for big N).
update() may loop over k (small), but try np.add.at / np.bincount for a loop-free version.

kmeans_plus_plus_init: first centroid uniformly at random from X; each next
centroid picked from X with probability proportional to D(x)^2, the squared
distance to the nearest centroid chosen so far.
"""

import numpy as np

from testkit import close, run


def pairwise_sq_dists(X: np.ndarray, C: np.ndarray) -> np.ndarray:
    """(N, D), (k, D) -> (N, k) squared Euclidean distances."""
    # TODO: your code here
    raise NotImplementedError


def assign(X, C) -> np.ndarray:
    """Index of the nearest centroid for each point, shape (N,)."""
    # TODO: your code here
    raise NotImplementedError


def update(X, labels, C_old) -> np.ndarray:
    """New centroids (k, D). Empty clusters keep their C_old row."""
    # TODO: your code here
    raise NotImplementedError


def kmeans_plus_plus_init(X, k, rng) -> np.ndarray:
    """(k, D) initial centroids, each one a row of X. Use rng (np.random.Generator)."""
    # TODO: your code here
    raise NotImplementedError


def kmeans(X, k, n_iters=100, tol=1e-6, init=None, seed=0):
    """Return (C, labels, inertia). If init is None use kmeans++ with default_rng(seed)."""
    # TODO: your code here
    raise NotImplementedError


# ----------------------------------------------------------------- tests ----

rng = np.random.default_rng(0)


def _blobs(n=60, centers=((0, 0), (10, 0), (0, 10)), std=0.5):
    X = np.concatenate([rng.normal(c, std, size=(n, 2)) for c in centers])
    y = np.repeat(np.arange(len(centers)), n)
    return X, y


def _same_partition(a, b):
    """True if labelings a and b are equal up to renaming the clusters."""
    pairs = set(zip(a.tolist(), b.tolist()))
    return len(pairs) == len(set(a.tolist())) == len(set(b.tolist()))


def test_dists():
    X, C = rng.normal(size=(20, 5)), rng.normal(size=(4, 5))
    brute = ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)
    d = pairwise_sq_dists(X, C)
    close(d, brute, what="dists")
    assert (pairwise_sq_dists(X, X).diagonal() >= 0).all(), "negative distances (clip round-off)"


def test_assign():
    X = np.array([[0.0, 0], [0.9, 0], [5, 5], [4, 6]])
    C = np.array([[5.0, 5], [0, 0]])
    assert assign(X, C).tolist() == [1, 1, 0, 0], assign(X, C)


def test_update_and_empty():
    X = np.array([[0.0, 0], [2, 0], [10, 10]])
    labels = np.array([0, 0, 2])
    C_old = np.array([[1.0, 1], [-7, -7], [0, 0]])
    close(update(X, labels, C_old), [[1, 0], [-7, -7], [10, 10]], what="centroids")


def test_kmeans_fixed_init():
    X = np.array([[0.0], [1], [2], [10], [11], [12]])
    C, labels, inertia = kmeans(X, 2, init=np.array([[0.0], [1.0]]))
    close(np.sort(C, 0), [[1], [11]], what="centroids")
    close(inertia, 4.0, what="inertia")
    assert _same_partition(labels, np.array([0, 0, 0, 1, 1, 1])), labels


def test_blobs():
    X, y = _blobs()
    C, labels, inertia = kmeans(X, 3, seed=1)
    assert _same_partition(labels, y), "didn't recover the 3 blobs"
    want = pairwise_sq_dists(X, C)[np.arange(len(X)), labels].sum()
    close(inertia, want, what="inertia")


def test_kmeanspp():
    X, _ = _blobs(n=30)
    C = kmeans_plus_plus_init(X, 3, np.random.default_rng(0))
    assert C.shape == (3, 2), f"shape {C.shape}"
    rows = {tuple(r) for r in X.tolist()}
    assert all(tuple(c) in rows for c in C.tolist()), "centroids must be points of X"
    hits = 0
    for s in range(20):
        lab = assign(X, kmeans_plus_plus_init(X, 3, np.random.default_rng(s)))
        hits += len(set(lab.tolist())) == 3 and _same_partition(lab, np.repeat([0, 1, 2], 30))
    assert hits >= 18, f"only {hits}/20 inits hit all 3 blobs - D^2 sampling wrong?"


if __name__ == "__main__":
    run("k-means (numpy)", [
        (test_dists, "pairwise_sq_dists matches brute force, no negatives"),
        (test_assign, "assign picks nearest centroid"),
        (test_update_and_empty, "update = cluster means, empty cluster keeps old"),
        (test_kmeans_fixed_init, "kmeans converges from a given init"),
        (test_blobs, "kmeans recovers 3 blobs, inertia correct"),
        (test_kmeanspp, "kmeans++ picks points of X spread over the blobs"),
    ])
