import numpy as np
from numpy.random import randn


x = 1
print(type(x)) # int
y = 2.26
print(type(y)) # float


# Other stuff
greeting = "Hello"
name = "bob"
message = greeting + " " + name
print(message)


# Boolean
# * equal == , not equal !=, “not”, “and”, “or”

# Loops
counter = 1
while counter < 10:
    counter = counter + 1
    print(counter)

for i in range(5):
    print(i)

mylist = [10, 100, 1000]
for jj in mylist:
    print("jj = ", jj)


# IF

x = randn()
answer = None # "None"
if x > 1:
    answer = "Greater than 1"
elif x < -1:
    answer = "Less than -1"
else:
    answer = "between -1 and 1"
print(x)
print(answer)


# List

list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "end"]
list2 = [1, 0.5, "ahoj", list1]

not_list = range(15) # Python 3 - same as xrange in Python 2 (range already creates list in Python 2)
list3 = list(range(15))
list4 = list(range(10, 21, 5))

len(list1)

## indexation
list2[3][2]
list1[-1] # negative indexation (-1 = last index)
list1[2:5] # creates new list
list1[:3]
list1[1:]
list1[::2]
list1[2:7]
list1[-8:7]
list1[-8:7]
list1[-8:-10]
list1[-8:-11:-1]
list1[2:7:-1]


# Tuples
# * are immutable
t1 = (1, 2, 's')
t1[2]


# Arrays
# * array in python vs array in numpy
# * in numpy => all data types have to be same (otherwise convertion occures)
# * slicing array (e.g. array1[2:4]) creates something pointing to array1    X    slicing list creates new list
a = np.array([1, 2, 1.5])


