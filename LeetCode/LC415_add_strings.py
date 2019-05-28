class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = self.string2int(num1) + self.string2int(num2)
        return str(res)
        
    def string2int(self, strings):
        res = 0
        for i in range(len(strings)):
            res = ord(strings[i]) - ord('0') + res * 10
        return res

print(Solution().addStrings('123', '123'))