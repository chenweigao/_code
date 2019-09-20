class Solution:
    def solution(self, alist, total):
        if len(alist) == 0:
            return 0
        sum1 = alist[0]
        res = []
        for i in range(1, len(alist)):
            if sum1 > total:
                sum1 = alist[i]
                res = []
            else:
                sum1 += alist[i]
            res.append(alist[i])
        return res

alist = [6, 1, 1, 1, 2, 2, 5]
total = 5
print(Solution().solution(alist, total))
        