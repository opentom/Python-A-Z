import numpy as np
import matplotlib.pyplot as plt

# Matrix

mat1 = np.reshape([1, 2, 3, 4, 5, 6], (2,3))
mat2 = np.array([['a', 'b', 'c'], ['d', 'e', 'f']])

print('mat1 =\n', mat1)
print('mat2 =\n', mat2)
print('mat2 reshape =\n', mat1.reshape((3,2)))
print('mat2 reshape =\n', mat1.reshape((3,2), order='F'))

print('mat1[1,0] =\n', mat1[1,0])
print('mat1[1][0] =\n', mat1[1][0])
print()


# Dictionary

dic1 = {'France':1, 'Spain':True, 'Germany':'ahoj'}
print('dic =', dic1)
print('dic[\'Spain\'] =', dic1['Spain'])
print()


# Matrix operations

m1 = np.array([ [1, 2, 3], [4, 5, 6] ])
m2 = np.array([ [2, 2, 3], [2, 1, 2] ])
m3 = m1 / m2
print('m3 =\n', m3)


# Visualization
# in order to plot results uncomment plt.show()
# %matplotlib inline # in jupyter notebook - inline plotting

x = [1, 2, 3, 4, 5, 6, 1, 2, 4, 16]

line1, = plt.plot(x, '-o')
line2, = plt.plot(x[-1:0:-1], c='black', ls='--', marker='s')
plt.figlegend((line1, line2), ('hello', 'hi'), 'lower right')
# plt.legend([line1, line2], ['ahoj', 'cau'])
plt.grid()
# plt.show()

plt.plot([1, 2, 3, 4, 5], label='myline')
# plt.legend()
# plt.legend([line1], ['series1'], bbox_to_anchor=[1, 0], loc='upper left') # explanation: http://stackoverflow.com/questions/25068384/bbox-to-anchor-and-loc-in-matplotlib
# plt.legend([line1], ['series1'], bbox_to_anchor=[1, 0])
plt.xticks([0, 1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'], rotation='vertical')
# plt.show()


# Functions
def myfun():
    for i in range(0,3):
        print('Hello, Hi')

myfun()