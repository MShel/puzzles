from itertools import product
'''
pythonic way
'''
'''
def pressingButtons(buttons):
    numPad = [""   ,""    ,"abc","def" ,"ghi","jkl",
              "mno","pqrs","tuv","wxyz"]
    charArr = [numPad[int(digit)] for digit in buttons]

    return [''.join(s) for s in product(*charArr) if s]
'''

def pressingButtons(buttons):
    numPad = ["", "", "abc", "def", "ghi", "jkl",
              "mno", "pqrs", "tuv", "wxyz"]
    charArr = [numPad[int(digit)] for digit in buttons]

    return allStrings(charArr)


def allStrings(charArr):
    # base cases: charArr only has 0 or one element
    if len(charArr) == 0:
        return []
    if len(charArr) == 1:
        return list(charArr[0])

    # find the list of strings
    remaining = allStrings(charArr[1:])
    output = []

    for start_char in charArr[0]:
        # place start_char at the beginning of each string in
        # remaining
        output += [start_char + s for s in remaining]
    return output

print(pressingButtons("42"))