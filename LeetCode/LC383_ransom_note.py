import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(magazine) - collections.Counter(ransomNote)

