"""Print out all the melons in our inventory."""

# ideally this actually pulls from database
from melons import melon_data

#print sorted(melon_data.items()) #for melon in melon_data
for melon in sorted(melon_data):
    print "\n{}:".format(melon.upper())
    for attribute, value in sorted(melon_data[melon].items()):
        print "    {}: {}".format(attribute, value)


"""

"""
