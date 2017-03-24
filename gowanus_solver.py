#python 2 !!! please note. Python TWO! NOT three

import random

class State:

    def __init__(self, nsize):
        """"Initialize the n-puzzle problem, with n-size value, tsize total nodes and initial goal state from n
        """"

        self.nsize = nsize
        self.tsize = pow(self.nsize, 2)
        self.goal = range(1, self.tsize)
        self.goal.append(0)

    def printst (self, st) :
        """"print the list in matrix format.""""

        for (index, value) in enumerate(st):
            print ' %s ' % value,
            if index in [x for x in range(self.nsize - 1, self.tsize, self.nsize)]:

                print

            print

    def getvalues(self, key)
        ""Utility function to gather the Free Motions at various key""

        values = [1, -1, self.nsize, -self.nsize]
        valid = []
        for x in values:
            if 0 <= key + x < self.tsize:
                if x ==1 and key in range(self.nsize - 1, self.tsize, self.nsize):
                    continue

            if x ==-1 and key in range(0, self.tsize, self.nsize):
                continue
                valid.append(x)

            return valid

        def expand(self, st):
            """Provide the list of next possible states from current state"""

            pexpands = {}
            for key in range(self.tsize):
                pexpands[key] = self.getvalues(key)
                pos = st.index(0)
                moves = pexpands[pos]
                expstates = []

                for mv in moves:
                    nstate = st[:]
                    (nstate[pos + mv], nstate[pos]) = (nstate[pos], nstate[pos+mv])
                    expstates.append(nstate)
                    return expstates

                def one_of_poss(self, st):
                    """Choose one of the possible states."""

                    exp_sts = self.expand(st)
                    rand_st = random.choice(exp_sts)
                    return rand_st
