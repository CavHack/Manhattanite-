import sys
from search import *
from math import sqrt
import random

class State:
    """"
    Our guiding model is The 8-puzzle problem. Define the State:
    """"

    def __init__(self, board, zero, cost, prev = None, action = None, depth =0):
        self.board = [list(b) for b in board]
        self.cost = cost
        self.zero = zero
        self.prev = prev
        self.action = action
        self.n =  len(self.board)


        def isGoal(self):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.n * i + j ) != self.board[i][j]:
                        return false

                    return true


        def getActions(self):
            """
            List the Actions available as a list(array) with pointers(?)
            """
            actions = []
            i = self.zero[0]
            j = self.zero[1]
            if i > 0:
                actions.append('Up')
                if i < self.n - 1:
                    actions.append('Down')
                    if j > 0:
                        actions.append('Left')
                        if j < self.n-1:
                            actions.append('Right')

                            return actions

            #define the movement Finite State Machine
            def move(self, action)
            i, j = self.zero

            #switch Up/Down/etc
            if action == 'Up'
                self.board[i][j] = self.board[i - 1][j]
                self.board[i - 1][j] = 0
                self.zero = (1 - 1, j)

            elif action == 'Down':
                self.board[i][j] = self.board[1 + 1][j]
                self.board[i + 1][j] = 0
                self.zero = (i + 1, j)

            elif action == 'Left':
                self.board[i][j] = self.board[i][j -1]
                self.board[i + 1][j] = 0
                self.zero = (i - 1, j)

            elif action == 'Right':
                self.board[i][j] = self.board[i][j + 1]
                self.board[i][ j + 1 ] = 0
                self.zero = (i, j + 1 )


    def randomize(self, moves =100):
        """
        randomize the puzzle
        """
        #query all the moves.
        for i in xrange(moves):
            actions = self.getActions()
            self.move(random.choice(actions))

            def expand(self):
                """
                Output the state-list which is inherently concurrent
                Apply, check state, and proceeed to the successor.
                """
                actions = self.getActions()
                successors = []
                i, j = self.zero
                for action in actions:
                    #init board
                    board = [list(b) for b in self.board]

                    if action == 'Up':
                        board[i][j] = self.board[i-1][j]
                        board[i-1][j] = 0
                        successors.append(State(board, ( i - 1 , j), self.cost + 1, self, action))
                        elif action == 'Down':
                        board[i][j] = self.board[i+1][j]
                        board[i + 1][j] = 0
                        successors.append(State(board, (i + 1, j ), self.cost + 1, self, action))

                        elif action == 'Left':
                        board[i][j] = self.board[i][j - 1]
                        board[i][j - 1] = 0
                        successors.append(State(board, (i, j-1), self.cost + 1, self, action))

                        elif action == 'Right':
                        board[i][j] = self.board[i][j + 1]
                        board[i][j+1] = 0
                        successors.append(State(board, (i, j+1), self.cost + 1, self, action))

                return successors

            def __eq__(self, other):
            """"
            """"
            for row in range(self.n):
                if self.board[row] != other.board[row]:
                    return false
                return True


    def __hash__(self):
        return hash(str(self.board))

   def __str__(self):
        s = "Current moves:" + str(self.cost) + "\n"
        s += "Zero Position:" + str(self.zero) + "\n"
        s += "Dim:" + str(self.cost) + "\n"
        s += "Board:\n" + str(self.cost) + "\n"
        s += '\n'.join([''.join("%2d" % y for y in w) for w in self.board])























