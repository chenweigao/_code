class SolutionDFS:
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


class SolutionMemoization:
    def findTargetSumWays(self, nums, S):
        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(
                        i + 1, s - nums[i]) + findTarget(i + 1, s + nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]

        cache = {}
        return findTarget(0, S)


class SolutionDP:
    '''
    This ways use the P(sum of positive nums) and N(sum of negative nums)

    sum(P) - sum(N) = target
    sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
    2 * sum(P) = target + sum(nums)

    so, the conclution is:
    find a subset P of nums such that sum(P) = (target + sum(nums)) / 2, where target + sum(nums) must be even.
    '''

    def findTargetSumWays(self, nums, s):
        total = sum(nums)

        if total < s or (s + total) % 2 != 0:
            return 0
        
        sub_sum = (total + s) // 2

        dp = [0 for _ in range(sub_sum + 1)]
        dp[0] = 1

        acc = 0
        for n in nums:
            acc += n
            for i in range(min(acc, sub_sum), n - 1, -1):
                dp[i] += dp[i - n]
        return dp[-1]




nums = [1, 2, 3, 4, 5]
S = 3

print("Solution DFS:", SolutionDFS().findTargetSumWays(nums, S))
print("Solution memo DFS:", SolutionMemoization().findTargetSumWays(nums, S))
print("Solution DP:", SolutionDP().findTargetSumWays(nums, S))
