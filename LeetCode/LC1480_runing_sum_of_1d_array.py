class Solution:
    def runningSum(self, nums: 'List[int]') -> 'List[int]':
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[i - 1] + nums[i])
        return res

nums = [1,2,3,4]
print(Solution().runningSum(nums))