# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 1 #pmt number

while principal > 0:
    if i < 13:
      principal = principal * (1+rate/12) - (payment + 1000)
      total_paid = total_paid + (payment + 1000)
    else:
      principal = principal * (1+rate/12) - payment
      total_paid = total_paid + payment 
        
    i = i + 1

print('Total paid',total_paid)
print('Number of months',i)
