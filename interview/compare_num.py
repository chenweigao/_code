class Solution:
    def solution(self, nums):
        res = []
        for num in nums:
            res.append(self.process_num(num))
        return max(res)

    def process_num(self, num):
        num_list = [int(_) for _ in str(num)]
        num_list.sort()
        res = 0
        for num in num_list:
            res = res * 10 + num
        return res
    
# nums = [9638, 8210, 331]
# print(Solution().solution(nums))

from builtins import input

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        print(Solution().solution(nums))
    except:
        break