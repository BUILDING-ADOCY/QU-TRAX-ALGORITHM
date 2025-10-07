"""Entry point demonstrating a simple optimization run."""

from .core import simulated_annealing
from .models import TSPProblem


def main() -> None:
    distance_matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0],
    ]
    problem = TSPProblem(distance_matrix)
    initial_route = list(range(len(distance_matrix)))
    best_route, best_cost = simulated_annealing(problem, initial_route)
    print("Best route:", best_route)
    print("Cost:", best_cost)


if __name__ == "__main__":
    main()
