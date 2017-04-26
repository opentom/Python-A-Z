import numpy as np

# #Data
# revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
# expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]
#
# # Data evaluation
# # round(), max, min
# profit = [] # in thousands
# profit_tax = [] # profit after tax in thousands
# profit_margin = [] # in %
#
#
# for i in range(0, len(revenue)):
#     profit.append((revenue[i] - expenses[i]) / 1000)
#     profit_tax.append(profit[i] * 0.7)
#     profit_margin.append(profit_tax[i]*1000*100 / revenue[i])
#
#
# mean = np.mean(profit_tax) # mean of profits after taxation
# print("mean =", mean)
# profit_tax_e = enumerate(profit_tax)
#
# bad_months = [i for i, x in profit_tax_e if x < mean]
# good_months = [i for i, x in profit_tax_e if x > mean]
#
#
#
#
#
#
#
# name_format_str = "{:23}"
#
# print(name_format_str.format("good months = "), end='')
# for i in range(len(good_months)):
#     print("{:d}, ".format(good_months[i]), end='')
# print()
#
# print(name_format_str.format("bad months = "), end='')
# for i in range(len(bad_months)):
#     print("{:d}, ".format(bad_months[i]), end='')
# print()
#
#
# print("profit_tax = ", profit_tax)
# print(profit_tax[2] < mean)


list1 = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']
print(list1[1::2])
print(list1[1:12:2])
print(list1[-1:-40:-2])