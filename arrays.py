my_list = [1,2,3]

import numpy as np

arr = np.array(my_list)
arr

array([1, 2, 3])
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
my_mat
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_mat
np.array(my_mat)
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])

// More array Practice

np.arange(0,11)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

np.arange(0,11,2)
array([ 0,  2,  4,  6,  8, 10])


// Making Arrays With Only Zero in Them

np.zeros(3)
array([0., 0., 0.])

np.zeros((5,5))
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
