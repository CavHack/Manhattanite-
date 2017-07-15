def update_u(u, v, d, n1, userDict):
#query ith item inside a n1 range
	for i in range(n1) 
		sumu1 = np.matrix(np.zeros((d,d)))
		 #coset...why? Think tuples
		sumu2 = np.matrix(np.zeros((d,1))) 
	#column search
		for j in userDict[i]: 

			sumu1 += np.matmul(np.matrix(v[j]).T, np.matrix(v[j]))
#vector1
	return u 

def update_v(u, v, d, n2, proDict):

	#column search the second stream.
	for j in range(n2):
		sumv1 = np.zeros((d,d))
		sumv2 = np.zeros((d,1))

#vector2
	return v


if __name__ == '__main__':

	#create the dictionary assigned to each user.
	user = {}

	#creating a dictionary for prod

	prod = {}