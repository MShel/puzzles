'''
Implement a function rotateArray(vector<int> arr, int r) 
which rotates the array by r places. 
'''
def rotateArray(array, k):
    result = array[k:]
    result.extend(array[:k])
    return result

print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
