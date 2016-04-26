# One Away: three types of edit on string: insertion, deletion and
# replacement of letter. Write a function to determine whether two
# strings are one edit (or zero edits) away.

def edit_test(str1, str2):
    """ return whether strings are at most one edit away from each other
    """
    len_diff = len(str1) - len(str2)
    if abs(len_diff) > 1:
        return False
    elif abs(len_diff) == 1:
        shorter, longer = str1, str2
        if len_diff == 1:
            shorter, longer = str2, str1
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                if longer[i+1:] != shorter[i:]:
                    return False
        return True
    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i+1:] != str2[i+1:]:
                    return False
        return True

###############
# Testing
###############

if edit_test("pale", "ple") is not True:
    print "failed test 1"
if edit_test("pales", "pale") is not True:
    print "failed test 2"
if edit_test("pale", "bale") is not True:
    print "failed test 3"
if edit_test("pale", "bake") is not False:
    print "failed test 4"
