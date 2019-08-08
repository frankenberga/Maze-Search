from Maze import Maze
from uninformed_search import bfs_search
from time import sleep

class BlindrobotProblem:
    def __init__(self, maze, goal_location):
        self.goal_location = goal_location
        self.maze = maze
        self.start_state = self.get_start_state(maze) 

    #this method gets the start state set for the blind robot problem which is any possible location in the maze
    def get_start_state(self, maze):
        self.maze = maze
        start_state_set = set()
        width = maze.width
        height = maze.height
        for x in range (0, width):
            for y in range (0, height):
                loc = (x, y)
                start_state_set.add(loc)
        return frozenset(start_state_set)

    #this method gets the successors for all possible states
    def get_successors_all(self, state):
        print state
        successor_list = []
        direction = 0
        while direction < 4:
            new_state_set = set()
            print new_state_set
            #get successer north
            if (direction == 0):
                for s in state:
                    x = s[0]
                    y = s[1] + 1
                    new_state = (x, y)
                    if (self.safe_state(new_state)):
                        new_state_set.add(new_state)
            #get successor south
            elif (direction == 1):
                for s in state:
                    x = s[0]
                    y = s[1] - 1
                    new_state = (x, y)
                    if (self.safe_state(new_state)):
                        new_state_set.add(new_state)
            #get successer west
            elif (direction == 2):
                for s in state:
                    x = s[0] - 1
                    y = s[1]
                    new_state = (x, y)
                    if (self.safe_state(new_state)):
                        new_state_set.add(new_state)
            #get successor east
            elif (direction == 3): 
                for s in state:
                    x = s[0] + 1
                    y = s[1]
                    new_state = (x, y)
                    if (self.safe_state(new_state)):
                        new_state_set.add(new_state)
            successor_list.append(frozenset(new_state_set))
            direction += 1
        return successor_list

    #this method checks to make sure the state is safe, i.e. it is inside the bounds of the maze
    def safe_state(self, state):
        if (state[0] >= 0 and state[0] < self.maze.width and state[1] >= 0 and state[1] < self.maze.height):
            return True
        return False
    
    #this method checks to see if the state is a goal state
    def goal_test(self, state):
        state = set(state)
        if (len(state) == 1):
            if (state.pop() == self.goal_location):
                return True


    #this heuristic is based off of the size of the state
    def setsize_heuristic(self, state):
        heuristic = 0
        heuristic = len(state)
        return heuristic


    def __str__(self):
        string =  "Blind robot problem: "
        return string

    #this animates the path
    def animate_path(self, path):
        # reset the robot locations in the maze
        print "robot loc", self.maze.robotloc
        for state in path:
            state = set(state)
            print state
            for loc in state:
                print loc
                self.maze.robotloc = tuple(loc)
                print(str(self))
                print "state in path", self.maze.robotloc
                sleep(1)
                print(str(self.maze))