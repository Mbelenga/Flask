bill = float(input('How much is the bill? '))
tax = float(input('What is the sales tax (percentage)? '))
tip = float(input('How much of a tip (percentage)? '))

tax_amount = (bill * tax) / 100  #calculate the tax
total = bill + tax_amount

tip_amount = (total * tip) / 100
total = total + tip_amount

total = round(total, 2)

print("The total bill is$ ", total)