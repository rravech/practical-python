# pcost.py
#
# Exercise 1.27
f = open('portfolio.csv','rt')
headers = next(f)
headers
shares_total = 0
total_purchase_cost = 0
price =
for line in f:
     total_purchase_cost = total_purchase_cost + (int(shares)*float(price))

print('Total cost ', total_purchase_cost)
