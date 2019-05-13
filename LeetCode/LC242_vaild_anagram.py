import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # dic1, dic2 = {}, {}

        # for ch in s:
        #     dic1[ch] = dic1.get(ch, 0) + 1

        # for ch in t:
        #     dic2[ch] = dic2.get(ch, 0) + 1

        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)

        return dic1 == dic2


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_list = list(set(s))

        for word in word_list:
            if s.count(word) != t.count(word):
                return False
        return True

s = "anagram"
t = "nagaram"

print(Solution().isAnagram(s, t))