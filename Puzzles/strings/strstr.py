'''
O(MN) time
M - len(test_str)
N - len(search_for)
'''
def strstr(test_str, search_for):
    str_len = len(test_str)
    search_len = len(search_for)
    for i in range(0, str_len):
        if test_str[i:(i+search_len):] == search_for:
            return i
        else:
            i += search_len
    return -1

'''
O(m+n) time
'''
def KnuthMorrisPratt(text, pattern):
    # allow indexing into pattern and protect against change during yield
    pattern = list(pattern)
    # build table of shift amounts(O(N)) -- prefix table
    shifts = [1] * (len(pattern) + 1)
    shift = 1
    for pos in range(len(pattern)):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
        print(shifts)
    # do the actual search
    startPos = 0
    matchLen = 0
    for char in text:
        while matchLen == len(pattern) or \
              matchLen >= 0 and pattern[matchLen] != char:
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            return startPos
    return -1

test_string = "CodefightsIsAwesome"
search_for = "IsA"

print(strstr(test_string, search_for))
print(KnuthMorrisPratt(test_string, search_for))