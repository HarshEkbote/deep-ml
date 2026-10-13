import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    n=len(a)
    if n==1:
        return a
    out=[0]*n
    for i in range(n-1):
        out[i]=float(a[n-1-i])
    return out
