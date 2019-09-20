class Solution:
    def solution(self, alist, capacity):
        count = 0
        i = 0
        remain = 0
        while i < len(alist):
            if alist[i] > remain:
                remain = capacity
                count += 1
            elif alist[i] <= remain:
                remain = capacity - alist[i]
                i += 1
        return count
    
# alist = [1, 2]
# capacity = 3
# 3 2 2 2 1
# 4
alist = [int(_) for _ in input().split()]
capacity = int(input())
print(Solution().solution(alist, capacity))