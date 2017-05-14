import time
from resource import getrusage, RUSAGE_SELF
from utils import *

class Problem:
    """
    This is an abstract class that helps us define all the required methods to apply search algorithms
    as seen in a traditional automated ML pipeline.
    """

    def getStartState(self):
        raise NotImplementedError

        def isGoalState(self):
            raise NotImplementedError

            def getSuccessors(self):
                raise NotImplementedError

                def getCostOfAction(self):
                    raise NotImplementedError


     class Solver:
         """
         This class contains methods that use search algorithms seen in a full-stack automated ML Pipeline
         """

         def __init__(self):
             self.path = []
             self.cost_of_path = 0
             self.nodes_expanded = 0
             self.fringe_size = 1
             self.max_fringe_size = 1
             self.search_depth = 0
             self.max_search_depth = 0
             self.running_time = 0
             self.max_ram_usage = 0

             def breadthFirstSearch(self, problem):
                 """
                 BFS Search Strategy implementation
                 """

                 start_time = time.time()
                 #init frontier Queue
                 frontier = Queue()
                 #get the starting state and add it to the Queue
                 frontier.enqueue(problem.getStartState())
                 explored = set()
                 #While the frontier is not empty, search for fringes and add these to the queue
                 while not frontier.isEmpty():
                     state = frontier.dequeue()
                     self.fringe_size -= 1
                     explored.add(state)

               if problem.isGoalState(state):
                   curr = state
                   path = []
                   while curr.prev != None:
                       path.insert(0, curr.action)
                       curr = curr.prev
                  self.cost_of_path = state.cost
