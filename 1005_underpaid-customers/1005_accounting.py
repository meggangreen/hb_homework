melon_cost = 1.00

def cust_payment_calc(payment_file):
    """Parse payment text file and calculate under-/over-payments.
    """

    cust_total = 0.0

    with open(payment_file) as payment_data:
        for line in payment_data:
            order_data = line.split('|')
            cust_name = order_data[1] # order[0] is the line number
            cust_quant = float(order_data[2])
            cust_paid = float(order_data[3])
            cust_expect = cust_quant * melon_cost
            if cust_expect != cust_paid:
                cust_total += (cust_paid - cust_expect)
                print "{} paid ${:.2f}, expected ${:.2f}".format(
                cust_name, cust_paid, cust_expect)

    if cust_total < 0: 
        print "\nAnd we are ${:.2f} in the hole!\n".format(cust_total)
    else:
        print "\nAnd we owe customers ${:.2f} in free melons!\n".format(cust_total)

cust_payment_calc("customer-orders.txt")