def replace_elements(source_list, dest_list):
    """
    Complete the function replace_elements, a function which takes in source_list
    and dest_list and mutates the elements of dest_list to be the elements at the
    corresponding index in source_list.

    dest_list always has a length greater than or equal to the length of
    source_list.

    >>> s1 = [1, 2, 3]
    >>> s2 = [5, 4]
    >>> replace_elements(s2, s1)
    >>> s1
    [5, 4, 3]
    >>> s3 = [0, 0, 0, 0, 0]
    >>> replace_elements(s1, s3)
    >>> s3
    [5, 4, 3, 0, 0]
    """
    "*** YOUR CODE HERE ***"
    pass


# example of a bimodal constructed from two gaussian processes
from numpy import hstack
from numpy.random import normal
from matplotlib import pyplot
# generate a sample
X1 = normal(loc=20, scale=5, size=3000)
X2 = normal(loc=40, scale=5, size=7000)
X = hstack((X1, X2))
# plot the histogram
pyplot.hist(X, bins=50, density=True)
pyplot.show()

pyplot.hist(X1, bins=50, density=True)
pyplot.show()

pyplot.hist(X2, bins=50, density=True)
pyplot.show()

X= X.reshape(-1, 1)
from sklearn.mixture import GaussianMixture
# fit model
model = GaussianMixture(n_components=2, init_params='random')
model.fit(X)



# predict latent values
yhat = model.predict(X)
# check latent value for first few points
print(yhat[:100])
# check latent value for last few points
print(yhat[-100:])
pyplot.hist(yhat, bins=50, density=True)
pyplot.show()



''''''
# 导入模块
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
# 构建测试数据
N = 200; pi1 = np.array([0.6, 0.3, 0.1])
mu1 = np.array([[0,4], [-2,0], [3,-3]])
sigma1 = np.array([[[3,0],[0,0.5]], [[1,0],[0,2]], [[.5,0],[0,.5]]])
gen = [np.random.multivariate_normal(mu, sigma, int(pi*N)) for mu, sigma, pi in zip(mu1, sigma1, pi1)]
X = np.concatenate(gen)