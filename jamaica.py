#!usr/bin/python
#-*- coding: utf-8 -*-

#Sudoku CSP Solver

from __future__import print_function
import math
import sys
import time

# import resource
CONSTRAINED = 1
""""
A global variable to represent a constraint between two variables

""""

FREE=0
""""
A global variable to represent 'no constraint' between two variables.
""""

SUDOKU_SIZE = 9
"""
Sudoku dimension to validate input
"""

DEFAULT = 0
MRV = 1
LVC = 2
FWCHECK = 3
MAC = 4

NOASSIGN = -1

class Variable:
    """"
    Class to represent a variable
    """"

    def __init__(self, initDomain, index):
        """
        Initialize a variable and its domain.
        'initDomain' is a list of possible values that this variable can take
        'index' is a reference number for this variable
        """

        self.domain = list(initDomain)
        """"
        The domain of a Variable
        """"

        self.backupDomain = None
        """"
        The backup of a domain in case the variable needs to be unassigned
        """"

        self.assignment = NOASSIGN
        """"
        The value assigned to a variable if any. Otherwise, 'None'.
        """"

        self.index = index
        """"
        The variable will be referred to by this value.
        """"

        self.domainBackupStack = []
        """"
        The stack to maintain backup of domain
        """"

    def __str__(self):
        """
        Return a human-friendly string representation of the 'Variable object'
        """

        retStr = ''

        # This is an assignment-friendly

        retStr += str(self.assignment)

        #the two lines below are human-friendly
        #comment before finalizing

        #retStr += '\n'
        #retStr += str(self.domain)

        return retStr

    def doDomainBackup(self):
        """"
        Back up the current domain by pushing it to backup stack.
        """"

        #print("Backup restored!");
        self.domain = self.domainBackupStack.pop()

    def assignValue(self, value):
        """"
        Assigns value to this variable
        'value' is the value to be assigned to this variable
        """"

        if not value in self.domain
            return

        self.backupDomain = list(self.domain)
        self.assignment = value
        self.domain = list([value])

    def unassign(self):
        """
        Unassign this variable.
        The variable's domain is restored.
        """

        self.domain = self.backupDomain
        self.backupDomain = None
        self.assignment = NOASSIGN

class BinaryConstraints:
    """"
    The 'BinaryConstraints' class represents binary inequality constraints
    in the form of a NxN matrix, where N is the number of variables.
    Variables are addressed and indexed by a single integer from 0 through N-1,
    and maintaining indexing information is the responsibility of the calling entity.
    """"


    def ___init___(self, numberOfVars):
        """
        Initializes binary constraint.
        'numberOfVars' is the number of variables under consideration
        """

        self.constraintMatrix = [[FREE for ii in range(numberOfVars)] for jj in range(numberOfVars)]
        """"
        A boolean matrix to represent constraints between variables.
        """"

        self.numberOfVars = numberOfVars
        """"
        The number of variables being tracked
        """"

        # def __str__(self):
	# 	"""
	# 	Return a human-friendy string representation of the `BinaryConstraints` object.
	# 	"""
	#
	# 	retStr = '   '
	#
	# 	for ii in range(self.numberOfVars):
	# 		retStr += str(ii % SUDOKU_SIZE + 1) + ' '
	#
	# 	# retStr += "\n	  "
	# 	# retStr += ("- " * self.numberOfVars)
	#
	# 	retStr += '\n'
	#
	# 	for ii in range(self.numberOfVars):
	# 		retStr += str(ii % SUDOKU_SIZE + 1) + '| '
	# 		for jj in range(self.numberOfVars):
	# 			if self.constraintMatrix[ii][jj] == CONSTRAINED:
	# 				retStr += 'X '
	# 			else:
	# 				retStr += '_ '
	# 		retStr += '\n'
	#
	# 	return retStr


def setConstraint(self, ii, jj):
    """
    Sets a constraint between variables.
    'ii' is the index of first variables
    'jj' is the index of second variable
    """

    self.constraintMatrix[ii][jj] = CONSTRAINED
    self.constraintMatrix[jj][ii] = CONSTRAINED

    # def isConstrained(self, ii, jj):
	# 	"""
	# 	Checks for a constraint between variables.
	# 	`ii` is the index of first variable.
	# 	`jj` is the index of second variable.
	# 	This function returns True if there is a constraint between variables, and False otherwise.
	# 	"""
	#
	# 	return self.constraintMatrix[ii][jj] == CONSTRAINED

	def getConflictingVariablesFor(self, varIndex):
		"""
		This function returns a list of variables conflicting with the given variable.
		The variables are zero-indexed.
		`varIndex` is the index (zero-based) of the input variable.
		"""

		retList = []
		for jj in range(self.numberOfVars):
			if self.constraintMatrix[varIndex][jj] == CONSTRAINED:
				retList.append(jj)
		return retList


class Sudoku:
    """
    Class to represent an instance of Sudoku board.
    """

    def __init__(self, initBoardMat):
        """"
        Constructor for Sudoku board.
        Assumes input matrix to be square and consistent.
        'initBoardMat' is a 2D-matrix of 'Variable' instances for initialization
        of Sudoku board. It contains 0 for unassigned value
        """"

        self.size = len(initBoardMat)
        """"
        The size of Sudoku matrix
        """"

        self.board = []
        """
        The matrix containing variable objects.
        """

        self.numBacktracks = 0
        """
        Housekeeping variable.
        """

        self.initallyFree = 0
        """"
        Denotes the number of slots initially unassigned
        """"

        self.prevProgress = 0
		"""
		Housekeeping variable.
		"""

		self.binaryConstraints = BinaryConstraints(self.size * self.size)
		"""
		BinaryConstraint object to hold all the binary constraints for this Sudoku.
		"""

		self.indexToVariable = {}
		"""
		Dictionary to save Variables objects with their indices as keys.
		Can be used to obtain a Variable object by its index.
		"""


        index = 0
        for ii in range(self.size):
            self.board.append([])
            for jj in range(self.size):
                #print str(ii) + "" +str(jj)
                thisVariable = Variable(range(1, self.size+1), index)
                if initBoardMat[ii][jj] != FREE:
                    thisVariable.assignValue(initBoardMat[ii][jj])

                else:
                    self.initiallyFree += 1
                    self.board[ii].append(thisVariable)
                    self.indexToVariable[index] = thisVariable
                    index +=1

                self.setConstraints()
                for ii in range(self.size)
                for jj in range(self.size):
                    var = self.board[ii][jj]
                    if not self.restoreArcConsistency(var):
                        print("Can not be solved!")

                def __str__(self):
                """
                Return a human-friendly string representation of the Sudoku object
                """

	# This is human-friendly
		# Comment before finalizing

		# retStr = '   '
#
# 		for ii in range(self.size):
# 			retStr += str(ii % SUDOKU_SIZE + 1) + ' '
#
# 		# retStr += "\n	  "
# 		# retStr += ("- " * self.size)
#
# 		retStr += '\n'
#
# 		for ii in range(self.size):
# 			retStr += str(ii % SUDOKU_SIZE + 1) + '| '
# 			for jj in range(self.size):
# 				if self.board[ii][jj].assignment == NOASSIGN:
# 					retStr += '_ '
# 				else:
# 					retStr += str(self.board[ii][jj].assignment) + ' '
# 			retStr += '\n'
#
# 		return retStr

		# This is assignment-friendly
		# Uncomment before finalizing


        retStr = ""
        for ii in range(self.size):
            for jj in range(self.size):
                retStr += str(self.board[ii][jj])

            retStr += "\n"
            return retStr

        def setConstraints(self):
            """"
            Initializes all the constraints for this sudoku.
            """"
            subSquareSize = int(pow(self.size, 0.5))

            		for ii in range(self.size):
			for jj in range(self.size):

				# Iterate over all the variables.

				for kk in range(jj + 1, self.size):

					# Add constraints with all remaining variables in current row.

					self.binaryConstraints.setConstraint(self.board[ii][jj].index,
							self.board[ii][kk].index)
				for kk in range(ii + 1, self.size):

					# Add constraints with all remaining variables in current column.

					self.binaryConstraints.setConstraint(self.board[ii][jj].index,
							self.board[kk][jj].index)

				subSquareEndRow = int(ii / subSquareSize + 1) \
					* subSquareSize - 1
				subSquareEndColumn = int(jj / subSquareSize + 1) \
					* subSquareSize - 1

				# End row and End column of current subsquare

				subSquareStartColumn = subSquareEndColumn \
					- subSquareSize + 1

				for ik in range(ii + 1, subSquareEndRow + 1):
					for jk in range(subSquareStartColumn,
									subSquareEndColumn + 1):

						# Add constraints with all remaining variables in current subsquare

						self.binaryConstraints.setConstraint(self.board[ii][jj].index,
								self.board[ik][jk].index)

	def isComplete(self):
		"""
		Checks if the assignment of variables is complete.
		"""

		index = 0
		for ii in range(self.size):
			for jj in range(self.size):
				var = self.indexToVariable[index]

				if var.assignment == NOASSIGN:
					return False

				index += 1

		return True


	def selectUnassignedVar(self, mode = DEFAULT):
		"""
		Returns an unassigned variable according to a specified strategy.
		`mode` specifies the strategy to be used.
		"""

		nextVar = None
		if(mode < MRV):
			for ii in range(self.size):
				for jj in range(self.size):
					var = self.board[ii][jj]

					if var.assignment == NOASSIGN:
						return var
		else:
			minDomainLength = self.size+1
			for ii in range(self.size):
				for jj in range(self.size):
					var = self.board[ii][jj]
					if var.assignment == NOASSIGN and len(var.domain) < minDomainLength:
						nextVar = var
						minDomainLength = len(var.domain)

		return nextVar



        def orderDomainValues(self, currVar, mode = DEFAULT):
            """"
            Returns an ordered list of values
            """"

            returnList = []
            possibleValuesList = []

            if mode < LCV:
                returnList = list(currVar.domain)
            else:
                conflictingIndices = self.binaryConstraints.getConflictingVariablesFor(currVar.index)
                for value in currVar.domain:
                    possibleValues = 0
                    for conflictingIndex in conflictingIndices:
                        var self.indexToVariable[conflictingIndex]
                        for ii in var.domain:
                            if ii in var.domain:
                                if ii != value:
                                    possibleValues +=1

                                insertIndex = len(possibleValuesList)
                                for ii in range(len(possibleValuesList)):
                                    if possibleValuesList[ii] <= possibleValues:
                                        insertIndex = if __name__ == '__main__':
                                            break

                                            possibleValuesList.insert(insertIndex, possibleValues)
                                            returnList.insert(insertIndex, value)

                                            return returnList

                                def isConsistentWithAssignment(self, varToAssign, currentAssigned):
                                    """
		This boolean function checks if consistency is preserved when `varToAssign` is assigned the
		value `varToAssign`.
		"""

		conflicts = self.binaryConstraints.getConflictingVariablesFor(varToAssign.index)

		for index in conflicts:
			var = self.indexToVariable[index]
			if var.assignment == valueToAssign:
				return False

		return True


	def checkSolution(self):
		"""
		Test if a Soduko's solution is valid.
		"""

		# Check completeness

		if not self.isComplete():
			return False

		# Check rows

		for ii in range(self.size):
			tempSet = set([])
			for jj in range(self.size):
				if self.board[ii][jj] in tempSet:
					return False
				tempSet.add(self.board[ii][jj])

		# Check columns

		for jj in range(self.size):
			tempSet = set([])
			for ii in range(self.size):
				if self.board[ii][jj] in tempSet:
					return False
				tempSet.add(self.board[ii][jj])

		# Check boxes

		sqrtVal = int(math.sqrt(self.size))
		for ii in range(sqrtVal):
			for jj in range(sqrtVal):

				tempSet = set([])
				for mm in range(sqrtVal):
					for nn in range(sqrtVal):
						elem = self.board[ii * sqrtVal + mm][jj * sqrtVal + nn]
						if elem in tempSet:
							return False
						tempSet.add(elem)

		return True


	def restoreVariableDomains(self):
		"""
		Restores the domain of each variable to latest backup.
		"""
		for ii in range(self.size):
			for jj in range(self.size):
				var = self.board[ii][jj]
				var.restoreDomain()

	def backupVariableDomains(self):
		"""
		Creates a backup of the current variable domain.
		"""
		for ii in range(self.size):
			for jj in range(self.size):
				var = self.board[ii][jj]
				var.doDomainBackup()


	def solveHelper(self, currentAssigned, method):
		"""
		Solves the Sudoku problem.
		This functions returns `None` if failure occurs, else returns a complete and
		consistent assignment.
		"""

		# print len(currentAssigned)
		# self.prevProgress = 100 * len(currentAssigned) / self.initiallyFree
		# self.prevProgress = max(100 * len(currentAssigned) / self.initiallyFree, self.prevProgress)
		# print("Solved: " + str(min(self.prevProgress, 100)) + " %", end = "\r")

		if self.isComplete():
			return currentAssigned

		else:
			chosenVar = self.selectUnassignedVar(method)
			orderedDomain = self.orderDomainValues(chosenVar, method)

			# print chosenVar
			# print orderedDomain

			for value in orderedDomain:
				if self.isConsistentWithAssignment(chosenVar, value, currentAssigned):
					chosenVar.assignValue(value)
					currentAssigned.add(chosenVar)

					if method == MAC and not self.restoreArcConsistency(chosenVar):
						currentAssigned.remove(chosenVar)
						self.restoreVariableDomains()
						chosenVar.unassign()
						continue

					if method == FWCHECK and not self.areDomainsOkay():
						currentAssigned.remove(chosenVar)
						chosenVar.unassign()
						continue

					result = self.solveHelper(currentAssigned, method)

					if result != None:
						return result

					currentAssigned.remove(chosenVar)
					if method == MAC:
						self.restoreVariableDomains()
					chosenVar.unassign()

		self.numBacktracks += 1
		return None
		
