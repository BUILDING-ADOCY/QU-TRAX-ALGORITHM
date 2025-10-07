from typing import Sequence


class TSPProblem:
    """Simple Traveling Salesman Problem representation."""

    def __init__(self, distance_matrix: Sequence[Sequence[float]]):
        self.distance_matrix = distance_matrix
        self.size = len(distance_matrix)

    def evaluate(self, route: Sequence[int]) -> float:
        """Return total distance for the given cyclic route."""
        cost = 0.0
        m = self.distance_matrix
        n = len(route)
        for i in range(n):
            cost += m[route[i]][route[(i + 1) % n]]
        return cost
