import re
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        re.match("(.+)\\1+", s)

print(Solution().repeatedSubstringPattern("abab"))