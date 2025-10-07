import random
import time

from qtrax.core import simulated_annealing
from qtrax.models import TSPProblem
from qtrax.utils import Timer


def make_problem():
    return TSPProblem([
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0],
    ])


def test_problem_evaluate():
    problem = make_problem()
    route = [0, 1, 2, 3]
    assert problem.evaluate(route) == 2 + 6 + 8 + 6


def test_simulated_annealing_improves():
    problem = make_problem()
    start_route = [0, 1, 2, 3]
    random.seed(0)
    best_route, best_cost = simulated_annealing(
        problem, start_route, initial_temp=10.0, cooling_rate=0.9, max_iterations=500
    )
    assert best_cost <= problem.evaluate(start_route)


def test_timer():
    with Timer() as t:
        time.sleep(0.01)
    assert t.elapsed() >= 0.01
