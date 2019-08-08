from MazeworldProblem import MazeworldProblem
from Maze import Maze

#from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

# test_maze2 = Maze("maze2.maz")
# print test_maze2
# test_mp = MazeworldProblem(test_maze2, (2, 2))
# print test_mp.robot1_table
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print result

test_maze3 = Maze("maze3.maz")
print test_maze3
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# print(test_mp.get_successors_all(test_mp.start_state))

#this should explore a lot of nodes; it's just uniform-cost search
# result = astar_search(test_mp, null_heuristic)
# print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.wavefront_heuristic)
print(result)
# test_mp.animate_path(result.path)

# Your additional tests here:

# test_maze01 = Maze("maze01.maz")
# print test_maze01
# test_mp = MazeworldProblem(test_maze01, (1, 2, 1, 1, 1, 0))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# test_maze02 = Maze("maze02.maz")
# print test_maze02
# test_mp = MazeworldProblem(test_maze02, (4, 0, 1, 0))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# test_maze03 = Maze("maze03.maz")
# print test_maze03
# test_mp = MazeworldProblem(test_maze03, (3, 5, 3, 5, 3, 5))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# test_maze04 = Maze("maze04.maz")
# print test_maze04
# test_mp = MazeworldProblem(test_maze04, (17, 16, 17, 18))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)

# test_maze05 = Maze("maze05.maz")
# print test_maze05
# test_mp = MazeworldProblem(test_maze05, (31,27))
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)