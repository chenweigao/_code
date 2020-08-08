class Solution:
    def numSub(self, s: str) -> int:
        res, count = 0, 0
        mod = 10**9 + 7
       
        for num in s:
            if num == '1':
                count += 1
            else:
                count = 0
            res = (res + count) % mod
        return res 
s = '0110111'
print(Solution().numSub(s))

