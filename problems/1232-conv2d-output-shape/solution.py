import math
def conv_out_shape(h, w, kernel, stride, padding):
    """Return (H_out, W_out) for a 2D conv with the given spatial params.

    Args:
        h: input height
        w: input width
        kernel: kernel size (same for H and W)
        stride: stride (same for H and W)
        padding: padding (same for H and W)

    Returns:
        Tuple of ints (H_out, W_out).
    """
    # TODO: apply the standard conv output-size formula
    if stride==0:
        return (0,0)
    h_out=math.floor((h+2*padding-kernel)/stride)
    w_out=math.floor((w+2*padding-kernel)/stride)
    return (h_out+1,w_out+1)