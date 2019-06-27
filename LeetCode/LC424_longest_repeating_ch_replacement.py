'''
题目大意是，给定一个字符串 AABABBA, 再给定一个整数 k
要计算出 k 次替换字符串中的字符后，得到的子串最长的长度
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = 0
        dic = dict()
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            # print(dic)
            freq = max(freq, dic[s[r]])
            # print(freq)
            # print(l, r)
            if r - l + 1 - freq > k:
                dic[s[l]] -= 1
                l += 1
        return len(s) - l # r - l 会出现空串不正确

s = 'AABABBA'
print(Solution().characterReplacement(s, 2))
