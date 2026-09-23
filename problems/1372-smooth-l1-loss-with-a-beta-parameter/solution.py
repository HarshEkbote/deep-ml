import numpy as np

def smooth_l1(pred, target, beta=1.0, reduction='mean'):
    """
    Elementwise Smooth L1 loss.

    Args:
        pred, target: arrays of the same shape
        beta: transition point between the quadratic and linear branches (> 0)
        reduction: 'mean', 'sum', or 'none'

    Returns:
        float for 'mean'/'sum', array for 'none'
    """
    pred=np.asarray(pred)
    target=np.asarray(target)
    if beta==0.0:
        raise ValueError("ValueError")
    x=pred-target
    result=np.where(np.abs(x)<beta,0.5*x**2/beta,np.abs(x)-0.5*beta)
    if reduction=="sum":
        return np.sum(result)
    elif reduction=="mean":
        return np.mean(result)
    elif reduction=="none":
        return result
    else:
        raise ValueError("ValueError")
