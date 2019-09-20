class Solution:
    def solution(self, a, b):
        if a < b:
            a, b = b, a
        
        t = a % b
        q = a * b
        while t:
            a = b
            b = t
            t = a % b
        return b, int(q / b)
        
# a = 25
# b = 65

a, b = [int(_) for _ in input().split()]


res1, res2 = Solution().solution(a, b)
print(res1, res2)