class Solution:
    count = 0
    def findTargetSumWays(self, nums, S):
        self.dfs(nums, S, 0, 0)
        return self.count

    def dfs(self, nums, S, sum, i):
        if i == len(nums):
            if sum == S:
                self.count += 1
        else:
            self.dfs(nums, S, sum + nums[i], i + 1)
            self.dfs(nums, S, sum - nums[i], i + 1)
            

nums = [1, 2, 3, 4, 5]
S = 3

print(Solution().findTargetSumWays(nums, S))