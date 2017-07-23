'''
def sortedSquaredArray(array):
    return sorted([x*x for x in array])

You have a sorted array of integers. Write a function that returns a sorted array containing the squares of those integers.
'''

def sortedSquaredArray(array):
    negs = []
    res = []
    for n in array:
        if n < 0:
            negs.insert(0, -n)
        else:
            while negs and negs[0] <= n:
                neg = negs.pop(0)
                res.append(neg*neg)
            res.append(n*n)
    return res


#arr = [-6, -4, 1, 8, 3, -5]
print(sortedSquaredArray([-7,-6,-5, -4, 1,3,8]))
