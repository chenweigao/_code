class Solution:
    # this solution time limited exceeded
    def maxArea(self, height: 'List[int]') -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height), 1):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res


class Solution2:
    def maxArea(self, height: 'List[int]') -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l <= r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res



height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print('Solution1 res is: ', Solution().maxArea(height))
print('Solution2 res is: ', Solution2().maxArea(height))