from SearchSolution import SearchSolution
from heapq import heappush, heappop
from astar_search import astar_search

class BlindNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic_fn, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.parent = parent
        self.heuristic_value = heuristic_fn
        self.transition_cost = transition_cost

    def priority(self):
        priority = self.transition_cost + self.heuristic_value
        return (priority)

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()

def blind_search(search_problem, heuristic_fn):
    start_node = BlindNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    