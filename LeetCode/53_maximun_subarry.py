class Solution:
    def maxSubArray(self, nums):
        max_so_far = nums[0]  # 最大值
        max_ending_here = nums[0]  # 位置
        s = 0  # strat
        e = 0  # end
        res = 0
        for i in range(1, len(nums)):
            if max_ending_here < 0:
                max_ending_here = 0
                s = i

            max_ending_here = max_ending_here + nums[i]

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                e = i
        for i in range(s, e + 1):
            res += nums[i]
        return max_so_far

    def maxSubArrayDP(self, nums):

        dp = [0 for _ in range(len(nums))]

        dp[0] = nums[0]
        max = dp[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] += nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            if max < dp[i]:
                max = dp[i]
        return max


data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArrayDP(data))
