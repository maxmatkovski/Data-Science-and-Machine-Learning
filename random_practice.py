import numpy as np

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

arr_2d

arr_2d[0][0]

arr_2d[0]

arr_2d[1][1]

arr_2d[1,1]

arr_2d[2,1]

arr_2d[:2,1:]

arr_2d[1:,1:]

arr = np.arange(1,11)

arr

arr > 5

bool_arr = arr > 5

bool_arr

arr[bool_arr]

arr[arr>5]

arr[arr < 3]


arr_2d = np.arange(50).reshape(5,10)

arr_2d

arr_2d[1:3]


