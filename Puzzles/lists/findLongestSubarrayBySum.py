def findLongestSubarrayBySum(s, arr):
    prefix = prefix_sum(arr)  # O(n)
    prefix_vals = dict((x, i) for i, x in enumerate(prefix))  # O(n)

    maxLength = -1
    maxPair = [-1]

    for i in range(1, len(prefix)):
        if s + prefix[i-1] in prefix_vals:
            j = prefix_vals[s+prefix[i-1]]
            if j - i > maxLength:
                maxLength = j - i
                maxPair = [i, j]

    return maxPair



def prefix_sum(arr):
    res = [0]
    for x in arr:
        res.append(res[-1] + x)
    return res

arr = [1, 2, 3, 7, 5]
s = 12

print(findLongestSubarrayBySum(s, arr))