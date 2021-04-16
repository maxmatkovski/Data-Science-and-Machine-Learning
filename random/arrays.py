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


// Linspace function
np.linspace(0,5,10)
array([0.        , 0.55555556, 1.11111111, 1.66666667, 2.22222222,
       2.77777778, 3.33333333, 3.88888889, 4.44444444, 5.        ])

// Creating arrays of random numbers

np.random.rand(5)
array([0.02324434, 0.65282984, 0.57734519, 0.78885581, 0.41117936])

np.random.rand(5,5)
array([[0.61659552, 0.40786887, 0.83658535, 0.50948273, 0.10491115],
       [0.46233951, 0.90400117, 0.05992038, 0.45426786, 0.00464822],
       [0.24613188, 0.15540585, 0.02757795, 0.45837289, 0.81042404],
       [0.74289063, 0.45887563, 0.29265795, 0.54025643, 0.34509322],
       [0.32788712, 0.89680417, 0.74347262, 0.97363914, 0.61086423]])

// Random Integer
np.random.randint(1,100)
39

np.random.rantint(1,100,10)
array([94, 72,  4, 32, 77, 42, 39, 21, 44, 29])


np.random.rand(5)

np.random.rand(5,5)



np.random.randint(1,100)

np.random.randint(1,100,10)


// More Array Practice

ranarr.min()

ranarr

arr.shape

arr.dtype

import numpy as np

arr = np.arrange(0,11)

arr = np.arange(0,11)

arr

arr[8]

arr[1:5]

arr[:6]

arr[0:6]

arr[5:]

arr[0:5] = 100

arr = np.arange(0,11)

arr

slice_of_arr = arr[0:6]

slice_of_arr

slice_of_arr[:]=99

slice_of_arr

arr

arr_copy = arr.copy()

arr

arr_copy[:] = 100

