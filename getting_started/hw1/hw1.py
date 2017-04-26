import numpy as np

#Data
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

profit = [] # in thousands
profit_tax = [] # profit after tax in thousands
profit_margin = [] # in %


for i in range(0, len(revenue)):
    profit.append((round(revenue[i], 2) - round(expenses[i], 2)) / 1000)
    profit_tax.append(round(profit[i] * 0.7, 2))
    profit_margin.append(profit_tax[i]*1000*100 / revenue[i])


mean = np.mean(profit_tax) # mean of profits after taxation
print("mean =", mean)

good_months = [i + 1 for i, x in enumerate(profit_tax) if x > mean]
bad_months = [i + 1 for i, x in enumerate(profit_tax) if x < mean]
best_month = [i + 1 for i, x in enumerate(profit_tax) if x == max(profit_tax)]
worst_month = [i + 1 for i, x in enumerate(profit_tax) if x == min(profit_tax)]

name_format_str = "{:23}"
print(name_format_str.format('profit = '), end='')
for i in range(len(profit)):
    print("{:.0f}k, ".format(profit[i]), end='')
print()

print(name_format_str.format("profit after tax = "), end='')
for i in range(len(profit_tax)):
    print("{:.0f}k, ".format(profit_tax[i]), end='')
print()

print(name_format_str.format("profit margin = "), end='')
for i in range(len(profit_margin)):
    print("{:.0f}%, ".format(profit_margin[i]), end='')
print()

print(name_format_str.format("good months = "), end='')
for i in range(len(good_months)):
    print("{:d}, ".format(good_months[i]), end='')
print()

print(name_format_str.format("bad months = "), end='')
for i in range(len(bad_months)):
    print("{:d}, ".format(bad_months[i]), end='')
print()

print(name_format_str.format("best month = "), best_month[0], sep='')
print(name_format_str.format("worst month = "), worst_month[0], sep='')
