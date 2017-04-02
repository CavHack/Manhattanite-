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
