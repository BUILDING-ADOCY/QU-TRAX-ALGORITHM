import random
from typing import List

def two_opt(route: List[int]) -> List[int]:
    """Return a new route by reversing a random subsequence (2-opt)."""
    if len(route) < 2:
        return route[:]
    i, j = sorted(random.sample(range(len(route)), 2))
    new_route = route[:]
    new_route[i:j+1] = reversed(route[i:j+1])
    return new_route
