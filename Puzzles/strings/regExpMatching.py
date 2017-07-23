'''
Implement regular expression matching with support for '.' and '*', given the following guidelines:
'.' Matches any single character.
'*' Matches zero or more of the element that comes before it.

For the 1st case, if the first char of pattern is not ".", the first char of pattern and string should be the same. 
Then continue to match the remaining part.

For the 2nd case, if the first char of pattern is "." or first char of pattern == the first i char of string,
continue to match the remaining part.
'''
def regularExpressionMatching(s, p):
    pattern_length = len(p)
    string_length = len(s)
    # base case
    if pattern_length == 0:
        return string_length == 0

    if pattern_length == 1:
        if string_length < 1:
            return False
        if p[0] != s[0] and p[0] != ".":
            return False
        return regularExpressionMatching(s[1:], p[1:])

    if p[1] != '*':
        # according to rules we got to have at list char before *
        #  and since * is at position 1 we got to match
        # something before it or anything in case of .
        if string_length < 1:
            return False
        if s[0] != p[0] and p[0] != ".":
            return False
        else:
            # matched the pattern move along to the next rule + pattern
            return regularExpressionMatching(s[1:], p[1:])
    else:
        if regularExpressionMatching(s, p[2:]):
            return True
        i = 0
        while i < string_length and (s[i] == p[0] or p[0] == '.'):
            if regularExpressionMatching(s[i + 1:], p[2:]):
                return True
            i += 1
        return False