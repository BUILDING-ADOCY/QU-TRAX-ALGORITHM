from qtrax.models import TSPProblem, Solution


def test_solution_dataclass():
    s = Solution(route=[0, 1, 2], cost=5.0)
    assert s.route == [0, 1, 2]
    assert s.cost == 5.0


def test_problem_size():
    matrix = [
        [0, 1],
        [1, 0],
    ]
    problem = TSPProblem(matrix)
    assert problem.size == 2
