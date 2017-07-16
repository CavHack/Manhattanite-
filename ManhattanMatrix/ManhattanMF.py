import __future__ import division
import numpy as np
import pandas as pd
import sys

def update_u(u, v, d, n1, userDict):
#query ith item inside a n1 range
	for i in range(n1) 
		sumu1 = np.matrix(np.zeros((d,d)))
	#coset...why? Think tuples
		sumu2 = np.matrix(np.zeros((d,1))) 
	#column search
		for j in userDict[i]: 

			sumu1 += np.matmul(np.matrix(v[j]).T, np.matrix(v[j]))
			sumu2 += ratings[i,j] * np.matrix(v[j]).T
	#index
			u[i] = np.matmul(np.linalg.inv(l * var * np.matrix(np.eye(d)) + sumu1), sumu2).T
	

	#vector1
	return u 

def update_v(u, v, d, n2, proDict):

	#column search the second stream.
	for j in range(n2):
		sumv1 = np.zeros((d,d))
		sumv2 = np.zeros((d,1))
		#in reverse now
			for i in prodDict[j]:

				sumv1 += np.matmul(np.matrix(u[i]).T, np.matrix(u[i]))
				sumv2 += np.matrix(ratings[i, j] * u[i]).T

				v[j] = np.matmul(np.linalg.inv(l * var * np.matrix(np.eye(d)) + sumv1), sumv2).T


#vector2
	return v





def calculateMaxLikelihood(data, u, v, nonZeroIndexes):
	sumObj1 = 0
	sumObj2 = 0
	sumObj3 = 0

	for [i,j] in nonZeroIndexes:
		sumObj1 += - 1 / 2( 2 * var ) * np.power(())

		sumObj1 += - 1 / 2( 2 * var ) * np.power(())

		










if __name__ == '__main__':

	#create the dictionary assigned to each user.
	user = {}

	#creating a dictionary for prod

	prod = {}