import heapq
'''
similar to LC414
'''


class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        nums.sort()
        return nums[-k]


class Solution2:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heapq.heappop(heap)
        # return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

print(Solution2().findKthLargest(nums, k))
