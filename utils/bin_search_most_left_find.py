'''
find the smallest one match
'''
def binarySearch(nums, target):

    if nums is None or len(nums) == 0:
        return -1

    start, end = 0, len(nums)
    while start + 1 < end:
        mid = start + (end - start) / 2
        if target > nums[mid]:
            start = mid
        else:
            end = mid
        #so in the normal case we would put elif here with == sign and return and else we would be elif with target < nums[mid]
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1

print(binarySearch([1,2,3,3,3,3,3,4,5,10], 3))