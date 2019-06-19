class Solution:
    def reverseVowels(self, s: str) -> str:
        alp = ['a', 'e', 'i', 'o', 'u']
        alp += [i.upper() for i in alp]
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l] not in alp:
                l += 1
            while l < r and s[r] not in alp:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)

s = "leetcode"
print(Solution().reverseVowels(s))