from heapq import heappush
import heapq

def kthLargestElement(nums, k):
    heap_list = []
    for num in nums:
        heappush(heap_list, num)

    k_largest = heapq.nlargest(k, heap_list)
    return k_largest[len(k_largest)-1]

print(kthLargestElement([3,2,1,4,5,6],2))