import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    return [float(A[i][i]) for i in range(len(A))]
