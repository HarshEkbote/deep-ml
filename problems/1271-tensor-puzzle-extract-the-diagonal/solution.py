import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    indices=np.arange(A.shape[0])
    diag=A[indices,indices]
    return diag
