cupcake_invoices = open('CupcakeInvoices.csv')

for cup in cupcake_invoices:
    print(cup)
    
for order in cupcake_invoices:
  splitorder = order.rstrip('\n').split(',')
  print(splitorder[2])

for order in cupcake_invoices:
  splitorder = order.rstrip('\n').split(',')
  print(float(splitorder[3])*float(splitorder[4]))

total = 0
running_total = 0
for order in cupcake_invoices:
  splitorder = order.rstrip('\n').split(',')
  total = (float(splitorder[3])*float(splitorder[4]))
  running_total += total
print(running_total)

cupcake_invoices.close()