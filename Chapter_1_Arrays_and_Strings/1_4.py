# Palindrone permutation
# Given a string, write a function to check whether it is
# a permutation of a palindrome. Case and spaces do not matter.

# Optimal solution here is again a bit-switching algorithm that
# runs through the string and for each character keeps track of whether
# that character has been seen an even or odd number of times.

def pal_check(str1):
    """ returns whether a string is a permutation of a palindrome
    This method makes use of fact that a character set can be a palindrome
    if at most one type of character appears an odd number of time. (The
    rest must appear an even number of times.)"""

    cleaned_str = "".join(str1.lower().split())
    odd_count = 0
    for x in set(cleaned_str):
        if cleaned_str.count(x)%2 == 1:
            odd_count += 1
        if odd_count == 2:
            return False
    return True

###############
# Testing
###############

if pal_check("Tact Coa") is not True:
    print "failed test 1"
if pal_check("Racecar") is not True:
    print "failed test 2"
if pal_check("tttaaa") is not False:
    print "failed test 3"
