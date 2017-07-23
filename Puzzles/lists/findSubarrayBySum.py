# remind me of: sliding window
# [head, tail]
# add tail to current sum
# 1.if current > s:
#   kick out head
#   compare again
# 2.if =:
# return
#
def findSubarrayBySum(s, arr):
    head = 0
    tail = 0
    curr = 0
    while tail < len(arr):
        curr += arr[tail]
        while curr > s:
            curr -= arr[head]
            head += 1
        if curr == s:
            return [head + 1, tail + 1]
        else:
            tail += 1
    return [-1]
