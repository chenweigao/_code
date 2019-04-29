class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashset = set()

        res = 0
        i, j = 0, 0

        while i < n and j < n:
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                hashset.remove(s[i])
                i += 1
        return res                
