# String compression


def compress(stri):
    """ return a compressed string using simple compression algo.
    Assume only characters a-z and A-Z can appear in strings
    """
    current_char, current_count = stri[0], 1
    compressed = []
    for index in range(len(stri)):
        if index == len(stri) - 1:
            compressed.append(current_char + str(current_count))
        elif stri[index+1] == stri[index]:
            current_count += 1
        else:
            compressed.append(current_char + str(current_count))
            current_count = 1
            current_char = stri[index + 1]
    compressed_string = "".join(compressed)
    if len(compressed_string) < len(stri):
        return compressed_string
    else:
        return stri

###############
# Testing
###############

if compress("aabcccccaaa") != "a2b1c5a3":
    print "failed test 1"

if compress("abcde") != "abcde":
    print "failed test 2"
