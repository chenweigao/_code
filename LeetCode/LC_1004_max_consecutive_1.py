'''
A = [1,1,1,0,0,0,1,1,1,1,0], K = 2

'''

class Solution:
    def longestOnes(self, nums: 'List[int]', k: int) -> 'int':
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1  # 右指针遇到 0 则继续向右移的同时，窗口内 0 的容量减 1

            if k < 0:   # 窗口内 0 的容量不够了
                if nums[l] == 1: # 如果左指针遇到 1, 左指针右移
                    l += 1
                elif nums[l] == 0: # 如果左指针遇到 0，右移的同时窗口内的容量加 1
                    l += 1
                    k += 1
        return r - l + 1
            

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(Solution().longestOnes(A, 3))

# simple version

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         l = 0
#         for r in range(len(nums)):
#             if nums[r] == 0:
#                 k -= 1
#             if k <0:
#                 if nums[l] == 0:
#                     k += 1
#                 l += 1
#         return r - l + 1
