
def parse_melon_delivs_files(filenames):
    """Print delivery information contained in each file.

    Parses delivery information contained in the specified
    file and formats the output to print each unique delivery
    on a single line.
    """
    # ideally would sort files by date so that day assignments correct
    i = 0
    for singlefile in filenames:
        i += 1
        print "Day {}".format(str(i))
        the_file = open(singlefile)
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')
            
            melon_type = words[0]
            melon_count = words[1]
            melon_income = words[2]

            print "Delivered {} {}s for total of ${}".format(melon_count, melon_type, melon_income)

        the_file.close()

parse_melon_delivs_files(["um-deliveries-20140519.txt","um-deliveries-20140520.txt","um-deliveries-20140521.txt"])

# EXTRA FUNCTION TO CHOOSE DIR AND VALIDATE FILE NAMES
# def create_melon_deliv_files_list(dirlocation):
#     """Cycle through all files in directory to create file list.

#     Cycles through the files in the specified directory to verify delivery files
#     (ideally, first sorts by date); then passes the filename to parse_melon_delivs_files
#     to format and print file content.
#     """
#     """But instead I just pass a list of file names
#     """
#     for filneame in dirname:
#         # with help from: http://thepythonguru.com/python-strings/
#         i = 0
#         if filename.startswith("um-") == True and filename.endswith(".txt") == True:
#             i += 1
#             print "Day {}".format(i)
#             parse_melon_delivs_files(filename)

# create_melon_deliv_files_list(.) # dirlocation hardcoded, but could be user input

"""ORIGINAL CODE
print "Day 1"
the_file = open("um-deliveries-20140519.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[1]
    amount = words[2]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()


print "Day 2"
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()


print "Day 3"
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print "Delivered {} {}s for total of ${}".format(
        count, melon, amount)
the_file.close()

"""
