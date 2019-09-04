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
            dic[s[r]] = dic.get(s[r], 0) + 1 # 统计某个字符的出现次数
            # print(dic)
            freq = max(freq, dic[s[r]]) # 到此为止的这个字符出现的次数
            # print(freq)
            # print(l, r)
            if r - l + 1 - freq > k: # 滑动窗口内可以容纳 k 个不同于该字符的
                l += 1  # 左指针右移，左指针可以容纳的它自己的字符数量 -1
                dic[s[l]] -= 1
        return len(s) - l # r - l 会出现空串不正确

'''
# 对比 LC1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k <0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1
'''


s = 'AABABBA'
print(Solution().characterReplacement(s, 2))
