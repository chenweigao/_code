class Solution:
    def solution(self, array):
        res = 0
        for num in array:
            res = max(res, num)
        l = 0
        r = 2 * res
        while l < r:
            mid = (l + r) // 2
            count = 0
            for num in array:
                count += max(mid - num, 0)
            if mid > count:
                l = mid + 1
            else:
                r = mid
        return max(l, res)
    def solution2(self, array):
        res = 0
        min_num = min(array)
        max_num = max(array)
        return max_num - min_num + min_num
# array = [2, 3, 4]

m = input()
array = [int(_) for _ in input().split()]

print(Solution().solution(array))
# print(Solution().solution2(array))
