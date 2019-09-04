class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 使用辗转相除法
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ''

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):],str2)

str1 = "ABABAB"
str2 = "ABAB"

print(Solution().gcdOfStrings(str1, str2))
