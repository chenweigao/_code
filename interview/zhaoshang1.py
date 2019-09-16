from itertools import combinations
import re
class Solution:
    def solution(self, s):
        nums = []
        nums.append(s)
        for s in nums:
            for ch in s:
                if ch == '?':
                    for i in range(10):
                        res = s.replace('?', str(i), 1)
                        nums.append(res)
        ret = []
        for s in set(nums):
            if '?' not in s:
                ret.append(s)
        count = 0
        for s in ret:
            if int(s) % 13 == 5:
                count += 1
        return count % (10 ** 9 + 7)


s = input()

print(Solution().solution(s))
