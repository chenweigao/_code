nums = [1, 7, 3, 6, 5, 6]


class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
        # S = sum(nums)
        # leftsum = 0
        # for index, num in enumerate(nums):
        #     if leftsum == (S - leftsum - num):
        #         return index
        #     leftsum += num
        # return -1
print(Solution().pivotIndex(nums))