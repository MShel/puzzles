'''
You have an array nums. We determine two functions to perform on nums. 
In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
Using these two functions, calculate all values of f modulo the given m. 
Take these new values and add them together to get g. 
You should return the value of g modulo the given m.
'''

'''
O(n)
'''
def productExceptSelf(nums, m):
    prefixProduct = [1] * len(nums)
    suffixProduct = 1  # now this is just a number

    # setup the cumulative product from left and right
    for i in range(1, len(nums)):
        # Need parenthesis, as % has higher precedence than *
        prefixProduct[i] = (prefixProduct[i - 1] * nums[i - 1]) % m

    total = 0
    for i in range(len(nums)):
        # start at the end, with prefixProduct -1
        # and scan right
        total += (prefixProduct[-1 - i] * suffixProduct) % m
        suffixProduct = (suffixProduct * nums[-1 - i]) % m
        # now multiply suffixProduct by the number that
        # was excluded

    return total % m
'''
O(N^2)
def productExceptSelf(nums, m, skip_i=0, res=[]):
    prd = 1
    for i in range(0, len(nums)):
        if i != skip_i:
            prd *= nums[i]
    res.append(prd)
    if len(nums) == len(res):
        return sum(res) % m
    else:
        skip_i += 1
        return productExceptSelf(nums, m, skip_i, res)
'''

nums = [1,2,3,4]
m = 12
#print(get_product(nums, m))
#print(get_summ(nums))
#print(24 % 12)
print(productExceptSelf(nums, m))
