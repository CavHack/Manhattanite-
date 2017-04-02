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
