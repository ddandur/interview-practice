# Problem 1.2 Check Permutation
# Note: fastest solution is to move through string and count
# how many times each character appears, and then compare counts
# at the end - faster than the nlog(n) sorting time, though sorting
# method here is easier to look at

def check_perm(str1, str2):
    """ Check whether one string is a permutation of another
    """
    return sorted(str1) == sorted(str2)
#############
# Testing
#############

if check_perm("string", "tsring") is not True:
    print "failed test 1"
if check_perm("string", "ring") is not False:
    print "failed test 2"
if check_perm("string", "string") is not True:
    print "failed test 3"
if check_perm("string  ", "  string") is not True:
    print "failed test 4"
if check_perm("1123", "123") is not False:
    print "failed test 5"
