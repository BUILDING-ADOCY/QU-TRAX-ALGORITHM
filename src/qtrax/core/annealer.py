import math
import random
from typing import Callable, List, Tuple

from ..models.problem import TSPProblem
from .neighbor import two_opt


def simulated_annealing(
    problem: TSPProblem,
    initial_route: List[int],
    *,
    initial_temp: float = 100.0,
    cooling_rate: float = 0.95,
    min_temp: float = 0.1,
    max_iterations: int = 1000,
    neighbor_func: Callable[[List[int]], List[int]] | None = None,
) -> Tuple[List[int], float]:
    """Simple simulated annealing algorithm for TSP."""
    if neighbor_func is None:
        neighbor_func = two_opt

    current = initial_route[:]
    current_cost = problem.evaluate(current)
    best = current[:]
    best_cost = current_cost

    temp = initial_temp
    iteration = 0
    while temp > min_temp and iteration < max_iterations:
        candidate = neighbor_func(current)
        candidate_cost = problem.evaluate(candidate)
        delta = candidate_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = candidate
            current_cost = candidate_cost
            if current_cost < best_cost:
                best = current
                best_cost = current_cost
        temp *= cooling_rate
        iteration += 1
    return best, best_cost
