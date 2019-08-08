from BlindrobotProblem import BlindrobotProblem
from Maze import Maze
from astar_search import astar_search


# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# test_maze2 = Maze("maze2.maz")
# print test_maze2
# test_mp = BlindrobotProblem(test_maze2, (2, 2))
# result = astar_search(test_mp, test_mp.setsize_heuristic)
# print result
# test_mp.animate_path(result.path)

test_maze07 = Maze("maze07.maz")
print test_maze07
test_mp = BlindrobotProblem(test_maze07, (1, 0))
result = astar_search(test_mp, test_mp.setsize_heuristic)
print result
test_mp.animate_path(result.path)

