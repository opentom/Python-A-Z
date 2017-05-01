import pandas as pd

# importing dataset

## Method 1 - specifying full file path
stats = pd.read_csv('C:\\Users\\glabka\\PycharmProjects\\Udemy\\Python_A-Z\\section5\\DemographicData.csv') # type == <class 'pandas.core.frame.DataFrame'>
## Method 2 - changing working directory
import os
print(os.getcwd())
# os.chdir('')



# Data frames

print('number of rows =', len(stats))
print('numebr of columns =', len(stats.columns))
print(stats.columns)
print('-------------------')
print(stats.head()) # first  5 rows
print('-------------------')
print(stats.head(7)) # first 7 rows
print('-------------------')
print(stats.tail())
print('-------------------')
print(stats.info())
print('-------------------')
print(stats.describe()) # gives mean, standard deviation etc.
print('-------------------')
print(stats.describe().transpose())
print('-------------------')
stats.columns = ['a', 'b', 'c', 'd', 'e'] # renaming columns

## subsetting dataframes in Pandas
stats[0:2] # rows
stats[:10]
stats[::-1] # reversing data frame
stats['a'] # column 'a'
stats[['a', 'b']] # columns 'a' and 'b'
print(stats[['b', 'a']].head())
print('-------------------')
stats.a # quick access to one column
subset1 = stats[4:10:2][['a', 'b', 'c']]
print(subset1)
print('-------------------')
subset2 = stats['a'][1:4]
print(subset2)
print('-------------------')

## basic operations with dataframes
result1 = stats.c + stats.d # row by row addition
print(result1.head())
print('-------------------')
stats['newCol'] = stats.c / stats.d
print(stats.head())
print('-------------------')
