import numpy as np


def compute_roc_curve(y_true, y_scores):
    y_true = np.asarray(y_true)
    y_scores = np.asarray(y_scores)

    # Validate inputs
    if y_true.ndim != 1 or y_scores.ndim != 1:
        raise ValueError("y_true and y_scores must be 1-dimensional")

    if len(y_true) != len(y_scores):
        raise ValueError("y_true and y_scores must have the same length")

    if not np.all(np.isin(y_true, [0, 1])):
        raise ValueError("y_true must contain only 0 and 1")

    if len(y_true) == 0:
        return [0.0], [0.0]

    # Number of positive and negative samples
    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    # Edge case: only one class is present
    if P == 0 or N == 0:
        return [0.0], [0.0]

    # Sort scores in descending order
    order = np.argsort(-y_scores, kind="stable")

    sorted_scores = y_scores[order]
    sorted_labels = y_true[order]

    # Cumulative TP and FP as threshold decreases
    tp = np.cumsum(sorted_labels == 1)
    fp = np.cumsum(sorted_labels == 0) 

    # Keep only the last sample for each unique score.
    # This is important because all samples having the same
    # score must be classified together at that threshold.
    distinct = np.r_[sorted_scores[:-1] != sorted_scores[1:],True]

    tp = tp[distinct]
    fp = fp[distinct]

    # Add the initial point corresponding to threshold = +infinity
    tpr = np.r_[0.0, tp / P]
    fpr = np.r_[0.0, fp / N]

    return fpr.tolist(), tpr.tolist()