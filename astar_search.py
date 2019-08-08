from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
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


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node, solution, final_visited_cost):
    solution = solution
    result = []
    solution.cost = final_visited_cost
    #print "final cost", solution.cost
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    solution.path = result
    return solution


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    start_node.transition_cost = 0
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = dict()
    visited_cost[start_node.state] = start_node
    
    #while there is something left in the queue
    while pqueue:
        node = heappop(pqueue) #pop off the lowest value thing
        if (node.transition_cost == -1):
            continue
        else:
            current_state = node.state #get the current state from that node
            visited_cost[current_state] = node #put the node into the dictionary with the state as the key
            if search_problem.goal_test(current_state): #if it is the goal
                return backchain(node, solution, node.transition_cost) #return the backchain solution
            successors_list = search_problem.get_successors_all(current_state) #generate the sucessors list
            for child in successors_list: #for each child
                if (type(child) == tuple): #so that this only does this check for the mazeworld and not the blind robot
                    if (child[1:] == current_state[1:]): 
                        new_cost = node.transition_cost #get the new cost
                    else:
                        new_cost = node.transition_cost + 1
                else:
                    new_cost = node.transition_cost + 1
                if (not visited_cost.has_key(child)):
                    new_node = AstarNode(child, heuristic_fn(child), node, new_cost) #create a new node with the new cost and the child
                    heappush(pqueue, new_node) #put that node onto the heap
                    visited_cost[child] = new_node #put it in the visited cost list
                elif (visited_cost.get(child).transition_cost > new_cost): #if the cost of the node already in the list is bigger than the new cost
                    new_node = AstarNode(child, heuristic_fn(child), node, new_cost) #create the new node
                    old_node= visited_cost[child] #get the old, worse node
                    old_node.transition_cost = -1 #make its transition cost -1 so it isn't pulled out of the heap
                    visited_cost[child] = new_node #make the value associated with the state in the dictionary be the new, better node 
                    heappush(pqueue, new_node) #push new node onto heap
                new_cost = 0 #resetting the new cost value
            solution.nodes_visited += 1 #increase the number of nodes visited
                
    return solution
        

