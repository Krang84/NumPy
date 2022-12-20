
import numpy as np

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe","Joe"])

# 2d array shape (7,4)
data = np.random.randn(7,4)

# return a boolean array 
names == "Bob"

# names length is 7 = 7 number of lines of data

# rerturn a (2,4) shape array
data[names=="Bob"]

