class Solution:
    def dp(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return nums[0]
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))


data = [1]
print(Solution().rob(data))
