
from collections import deque
from SearchSolution import SearchSolution

# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.level = 0
    
# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def find_path(node):
    path = list()
    #while there is still a parent and we are not at the original node
    while (node.parent != None):
        #add the state to the path
        path.append(node.state)
        #repeat for the parent of that node
        node = node.parent
    #reverse the path so it starts at start and goes to goal
    path.reverse()
    return path

def bfs_search(search_problem, table, start_state):
    #get the start state and wrap it in a SearchNode
    start = SearchNode(start_state)
    #instantiate the fronteir and explroed dictionary
    fronteir = list()
    explored = set()
    #append the node to the fronteir
    fronteir.append(start)
    #while there is still something in the fronteir
    while fronteir:
        #pop it off, increment the number of nodes visited and add the state to the explored set
        node = fronteir.pop(0)
        explored.add(node.state)
        if ((table[node.state[1]][node.state[2]] > node.level) or (table[node.state[1]][node.state[2]] == 1000)):
            table[node.state[1]][node.state[2]] = node.level
        current_state = node.state
        #generate the sucessors list
        print current_state
        successors_list = search_problem.get_successors_all(current_state)
        #for each child in the list
        for child in successors_list:
            #if its not in the frontier nor the explored list
            if ((child not in fronteir) and (child not in explored)):
                new_node = SearchNode(child)
                new_node.parent = node
                new_node.level = node.level + 1
                fronteir.append(new_node)
    return table
     