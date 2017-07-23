def kpalindrome(s, k):
    if k == 0:
        if s != s[::-1]:
            return False
        return True
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return kpalindrome(s[1:], k - 1) or kpalindrome(s[:-1], k - 1)
    return kpalindrome(s[1:-1], k)