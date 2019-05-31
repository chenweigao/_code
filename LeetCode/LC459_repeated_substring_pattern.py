import collections
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        dic = collections.Counter(s)
        return dic


s = 'abcabcabcabc'
print(Solution().repeatedSubstringPattern(s))
