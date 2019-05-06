class Solution:
    def mySqrt(self, x):
        if x <= 1:
            return x
        l, r = 0, x

        while r - l > 1:
            mid = (r + l) // 2
            if x / mid >= mid:
                l = mid
            else:
                r = mid
        return l


print(Solution().mySqrt(4))
