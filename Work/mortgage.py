# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 1 #pmt number
extra_payment_start_month = input('Enter Month/Payment Number to start extra payment')
extra_payment_end_month = input('Enter Month Number/Payment Number to end extra payment')
extra_payment = input('Enter Extra Payment Dollar Amount')

while principal > 0:
    if i >= extra_payment_start_month and i <= extra_payment_end_month:
      principal = principal * (1+rate/12) - (payment + extra_payment)
      total_paid = total_paid + (payment + extra_payment)
    else:
      principal = principal * (1+rate/12) - payment
      total_paid = total_paid + payment
        
    i = i + 1

print('Total paid',total_paid)
#print('Number of months',i)
