import numpy as np

def top_quartile_mask(scores: list) -> list:
    """
    Return a boolean list marking scores in the top quartile (>= 75th percentile).
    """
    if len(scores)==0:
        return []
    percentile_75=np.quantile(scores,0.75)
    return list(scores>=percentile_75)