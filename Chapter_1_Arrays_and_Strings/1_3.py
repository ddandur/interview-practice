# URLify - write a method to replace all spaces in a string
# (including multiple spaces) with %20

def urlify(str):
    """ return a string with spaces replaced by %20
    """
    split_string = str.split()
    return "%20".join(split_string)



###############
# Testing
###############

if urlify("Mr John Smith     ") != "Mr%20John%20Smith":
    print "failed test 1"
