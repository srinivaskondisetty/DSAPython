import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-elm for elm in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
    
solution = Solution()
output = solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print('output', output)
    