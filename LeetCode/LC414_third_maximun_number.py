class Solution:
    def thirdMax(self, nums: 'List[int]') -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

nums = [10, 2, 2, 3, 1, 4, 4, 5]

print(Solution().thirdMax(nums))
