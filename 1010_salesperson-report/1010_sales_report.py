"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

melons_per_person = {}

sales_file = open("sales-report.txt")
for line in sales_file:
    line = line.rstrip()
    # entries = line.split("|")
    # https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch01s01.html
    person, dollar, quantity = line.split("|") # inline unpack
    melons_per_person[person] = melons_per_person.get(person, int(quantity)) + int(quantity)

sales_file.close()

for person, quantity in melons_per_person.iteritems():
    print "{} sold {:,} melons.".format(person, quantity)
