from Maze import Maze
from time import sleep
from uninformed_search import bfs_search

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.goal_locations = goal_locations
        self.maze = maze
        self.maze.robotloc.insert(0, 0) #this inserts which robots turn it is as the first value in the tuple
        self.start_state = tuple(maze.robotloc)
        #these tables are going to store the bfs heuristic values from wavefront planning
        self.robot1_table = None
        self.robot2_table = None
        self.robot3_table = None
        #this updates the tables based on the number of robots there are in the maze
        for i in range (0, len(goal_locations)/2):
            if (i == 0):
                self.robot1_table = self.wavefront_planning(table = self.create_empty_table(self.maze), maze = self.maze, goal_loc = self.goal_locations[0:2])
            elif (i == 1):
                self.robot2_table = self.wavefront_planning(table = self.create_empty_table(self.maze), maze = self.maze, goal_loc = self.goal_locations[2:4])
            elif (i == 2):
                self.robot3_table = self.wavefront_planning(table = self.create_empty_table(self.maze), maze = self.maze, goal_loc = self.goal_locations[4:6])
    
    #this method gets all of the successors no matter if there is one robot or three
    def get_successors_all(self, state):
        if (len(state) == 3):
            return self.get_successors(state)
        else:

            return self.get_successors_multi(state)
    
    #this method gets the successosr for one robot
    def get_successors(self, state):
        self.maze.robotloc = list(state)
        successor_list = [state]
        direction = 0
        while direction < 4:
            #get successer north
            if (direction == 0):
                x = state[1]
                y = state[2] + 1
            #get successor south
            elif (direction == 1):
                x = state[1]
                y = state[2] - 1
            #get successer west
            elif (direction == 2):
                x = state[1] - 1
                y = state[2] 
            #get successor east
            elif (direction == 3): 
                x = state[1] + 1
                y = state[2] 
            if self.safe_state(x,y):
                new_state = (0,x,y)
                #print new_state
                successor_list.append(new_state)
            direction += 1
        return successor_list

    #this robot gets the successors for multiple robots
    def get_successors_multi(self, state):
        self.maze.robotloc = list(state)
        #this deals with updating the robot number
        robot_num = state[0]
        if (robot_num == len(state)/2 -1):
            next_robot_num = 0
        else:
            next_robot_num = robot_num + 1
        robot_loc_moving = (state[robot_num*2 +1], state[robot_num*2 + 2])
        new_state = (next_robot_num,) + state[1:]
        successor_list = [new_state]
        direction = 0
        while direction < 5:
            #get successer north
            if (direction == 0):
                new_x = robot_loc_moving[0]
                new_y = robot_loc_moving[1] + 1
            #get successor south
            elif (direction == 1):
                new_x = robot_loc_moving[0]
                new_y = robot_loc_moving[1] - 1
            #get successer west
            elif (direction == 2):
                new_x = robot_loc_moving[0] - 1
                new_y = robot_loc_moving[1]
            #get successor east
            elif (direction == 3):
                new_x = robot_loc_moving[0] + 1
                new_y = robot_loc_moving[1]
            if self.safe_state(new_x, new_y):
                new_state = (next_robot_num,) + state[1:robot_num*2+1] + (new_x,new_y) + state[robot_num*2+3:]
                successor_list.append(new_state)
            direction += 1
        
        return successor_list

    #this method tests if a state is safe, only by checking that the robot location that was just moved is safe
    def safe_state(self, x, y):
        if (self.maze.is_floor(x, y) and not self.maze.has_robot(x, y)):
            return True
        return False

    #this method tests if a state is a goal, matching each agent to its specific goal 
    def goal_test(self, state):
        correct_goals = 0
        x = 1
        if (len(state) == 3):
            if (self.goal_locations[x-1] == state[x] and self.goal_locations[x] == state[x+1]):
                return True
        else:
            while (x < len(state)):
                if (self.goal_locations[x-1] == state[x] and self.goal_locations[x] == state[x+1]):
                    correct_goals += 1
                x += 2
            if (correct_goals == len(state) / 2):
                return True
        return False

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        print "robot loc", self.maze.robotloc
        self.maze.robotloc = tuple(self.maze.robotloc)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            print "state in path", self.maze.robotloc
            sleep(1)

            print(str(self.maze))
    
    #this is the simpler manhattan heuristic which returns the summed distances of each robot to its goal state
    def manhattan_heuristic(self, state):
        heuristic = 0
        if (len(state) == 3):
            heuristic = (abs(state[1] - self.goal_locations[0])) + abs((state[2] - self.goal_locations[1]))
            return heuristic
        else:
            for x in range (0, len(state) -1,2):
                value = abs(self.goal_locations[x] - state[x + 1]) + abs(self.goal_locations[x + 1] - state[x + 2])
                heuristic += value
            return heuristic
    
    #this is the wavefront heuristic which basically just sums the values obtained from the previously created robot tables 
    def wavefront_heuristic(self, state):
        heuristic = 0
        #it only sums up for the number of robots that are actually in the maze
        for i in range (0, len(state)/2):
            if (i ==0):
                heuristic += self.robot1_table[state[1]][state[2]]
            if (i == 1):
                heuristic += self.robot2_table[state[3]][state[4]]
            if (i == 2):
                heuristic += self.robot1_table[state[5]][state[6]]
        return heuristic

    
    #this method creates the wavefront table by using a bfs for a specific goal location
    def wavefront_planning(self, table, maze, goal_loc):
        current_search = self
        goal_loc = (0,) + goal_loc
        table = bfs_search(current_search, table, goal_loc)
        return table

    #this method creates an empty table for the wavefront planner to then add elements to
    def create_empty_table(self, maze):
        arr = []
        for i in range(0, self.maze.width):
            x = []
            for j in range(0, self.maze.height):
                x.append(1000)
            arr.append(x)
        return arr
            


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    # print(test_mp.get_successors_all((0, 1, 0, 1, 2, 2, 1)))
    
    # test_maze2 = Maze("maze2.maz")
    # print test_maze2
    # test_mp = MazeworldProblem(test_maze2, (2, 2))

    print (test_mp.robot1_table)
    print (test_mp.robot2_table)
    print (test_mp.robot3_table)
