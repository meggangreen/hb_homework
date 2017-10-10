"""Print out all the melons in our inventory."""

# ideally this actually pulls from database
from melons import melon_data

# print all attributes by sorted attribute name for each melon
for melon in sorted(melon_data):
    print "\n{}:".format(melon.upper())
    for attribute, value in sorted(melon_data[melon].items()):
        print "    {}: {}".format(attribute, value)


"""

"""
