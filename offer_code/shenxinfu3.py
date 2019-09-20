class Solution:
    def solution(self, alist, num):
        if not alist:
            return 0
        alist = list(set(alist))
        alist.sort(key=len, reverse=True)
        i = 0
        len_list = [len(_) for _ in alist]
        len_list = list(set(len_list))[::-1]
        return len_list
        if num - 1 < len(len_list):
            res = len(alist[num - 1])
            ret = []
            for s in alist:
                if len(s) == res:
                    ret.append(s)
            return ret
        
        return len(alist[0])

# alist = input().split()
# num = int(input())

alist = ['abc', 'ab', 'ab', 'cd', 'a', 'b']
print(Solution().solution(alist, 3))
