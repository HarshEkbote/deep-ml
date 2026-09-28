import numpy as np

def linspace(start, stop, n: int) -> np.ndarray:
    """n evenly spaced values from start to stop inclusive."""
    # Your code here
    if n<=0:
        return []
    if n==1:
        return [start]
    
    divisor=(n-1) if stop else n
    step=(stop-start)/divisor
    return [start+i*step for i in range(n)]

    
