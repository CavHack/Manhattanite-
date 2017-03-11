""""
Multiple strategies to solve the N-Puzzle: we aim to program a set of
informed/uninformed search strategies for combinatorial game theory applications
which ultimately rely on DFS, BFS, etc, notwithstanding, they aught to stand as
'tried and tested' functionals addressing: efficient adversarial graph traversal
with varying utility, but almost always less
efficient than other well-known A* algorithms. Moreover, the programming
of a FSM of earch stragies is a heuristically optional procedure which gives the
end user, a highly performant automaton with kidneys exposed; Fossils for
exploration.

*Mfrontier: The nodes at the frontier, fringe, or border of interest.
In this particular case, mathematically speaking, a closed haussdorf set.

*MMemory: The set of values that once traversed and backed up in some way.
*MTravis: A change within the N-puzzle board
*MSucc: Explicitly stated as the successor.
*MHeu: A heuristic function.


""""

from gyro import up, down, left, right
from collections import deque
from bisect import bisect_left, insort
from queue import PriorityQueue, Empty
import heuristics

class State_Node(nodeObject):
        def __init__(self, state, parent , travis):
            self.state = state
            self.parent = parent
            self.travis = travis
            self.num_NodeParents=0 if nodeParent == None else nodeParent.num_NodeParents+1

            # priority sorting switch
        def __lt__(self, other): return False;

    def _binaryIndex_rank(collection, value):
        ""
        A Binary search which scrapes rank index to facilitate its traversal through space.
        ""
        i = bisect_left(collection, value)
            if i != len(collection) and collection[i] == value:
                return i

            return None

    def _valid_State(state, haussdorf_set)
        return (state != None and
         _binaryIndex_rank(haussdorf_set, state) == None)

    def _doSearch(initState, desiredState, haussdorf_set_off, haussdorf_set_off_add)

        def haussdorf_set_off_add_if_not_visited(MSucc, travis):
            if _valid_State(MSucc, haussdorf_set):
