# Problem 1.1: Is Unique

# Fastest solution assumes a particular character set (e.g., unicode)
# and goes through string on element at a time, noting when each character
# has been used returning False if that character is used again.
# The sorting solution below takes nlog(n) time for the sort, whereas
# the checking algorithm takes costant time.

def all_unique(x):
    """
    Determines whether a string has all unique characters
    """
    assert type(x) == str, "Input must be a valid string"
    # print len(x) == len(set(x))
    return len(x) == len(set(x))


# if problem must be done without additional data structures besides strings


def all_unique_only_strings(x):
    """ Determines whether a string has all unique characters
    using only strings as data structures
    """
    sorted_string = sorted(x)
    for x, y in zip(sorted_string, sorted_string[1:]):
        if x == y:
            return False
    return True


###############
# Testing
###############

if all_unique("string") is not True:
    print "failed test 1"
if all_unique("stringg") is not False:
    print "failed test 2"
if all_unique("string ") is not True:
    print "failed test 3"
if all_unique("string  ") is not False:
    print "failed test 4"
if all_unique("abcdd") is not False:
    print "failed test 5"


if all_unique_only_strings("string") is not True:
    print "failed only strings test 1"
if all_unique_only_strings("stringg") is not False:
    print "failed only strings test 2"
if all_unique_only_strings("string ") is not True:
    print "failed only strings test 3"
if all_unique_only_strings("string  ") is not False:
    print "failed only strings test 4"
if all_unique_only_strings("abcdd") is not False:
    print "failed only strings test 5"
