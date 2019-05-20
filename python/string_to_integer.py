class Solution:
    def strToInt(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        
        ret = 0
        for c in s:
            if c == '-' or c == '+':
                continue
            if c < '0' or c > '9':
                return 0
            ret = ret * 10 + (ord(c) - ord('0'))

        return - ret if s[0] == '-' else ret
        

print(Solution().strToInt('109'))