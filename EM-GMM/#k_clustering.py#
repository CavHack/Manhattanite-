##############################################################################################################
# Author: Karl Whitford
#
# Manhattanite- Multi-disciplinary Machine Learning/A.I Toolkit with Python
#
# Extracted from project description:
# WHAT YOUR PROGRAM OUTPUTS
#
# You should write your K-means and EM-GMM codes to learn 5 clusters. Run both algorithms for 10 iterations. 
# You can initialize your algorithms arbitrarily. We recommend that you initialize the K-means centroids by 
# randomly selecting 5 data points. For the EM-GMM, we also recommend you initialize the mean vectors in the 
# same way, and initialize pi to be the uniform distribution and each Sigma_k to be the identity matrix.  
##############################################################################################################

import sys
import numpy as np

def load_data(input_file):
    """
    Load the dataset. Assumes a *.csv is fed without header, and the output variable in the last column
    """
    data = np.genfromtxt(input_file, delimiter=',', skip_header=0, names=None)
    return data

def KMeans(X, K=5, maxit=10, saveLog=true):
    """
    Apply KMeans for clustering a dataset given as input, and the number of clusters (K).
    Input: x1, ..., xn where x in R^d, and K
    Output: Vector c of cluster assignments, and K mean vectors mu
    """

    #Sample size
    N = X.shape[0]

    #Initialize output variable
    c = np.zeros(N)
    mu = X[np.random.choice(N, K, replace=False), :]

for i in xrange(N):
    kmin = 1
    minDist = float('Inf')
    for k in xrange(K):
        dist = np.linalg.norm(X[i, :] - mu[k, :])
        if dist < minDist:
            minDist = dist
            kmin = k

    c[i] = kmin + 1

    cNew = np.zeros(N)

    it = 1
    while it <= maxit and not all (c==cNew):
        #write the output file if required
        if saveLog:
            with open('centroids-'+ str(it) + '.csv', 'w') as f:
                for mu_i in mu:
                    for j in xrange(len(mu_i)-1):
                        f.write(str(mu_i[j]) + ',')
                        f.write(str(mu_i[len(mu_i) -1 ]) + '\n')

        c = np.copy(cNew)
        for i in xrange(N):
            kmin = 1
            minDist = float('Inf')
            for k in xrange(K):
                dist = np.linalg.norm(X[i, :]-mu[k, :])
                if dist < minDist:
                    minDist = dist
                    kmin = k

            cNew[i] = kmin + 1
        
        for k in xrange(1, K+1):
            Xk = X[cNew ==k, :]
            mu[k - 1] = np.sum(Xk, axis=0) / Xk.shape[0]
            it += 1

        return (c, mu, it)

def gauss(mu, cov, x):
    """
    Computes gaussian parametrized by mu and cov, given x. Make sure
    x dimensions are of correct size
    """
    d = len(x)
    den = np.sqrt(np.linalg.det(cov))*(2*np.pi)**(0.5*d)
    num = np.exp(-0.5 * np.dot(x-mu, np.linalg.solve(cov, np.transpose(x-mu))))
    return num/den

