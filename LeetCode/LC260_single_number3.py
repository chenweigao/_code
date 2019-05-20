class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        res = 0

        for num in nums:
            res ^= num
        res &= -res # 求 res 的二进制从右往左数第 1 个出现的 '1'

        rst = [0, 0]

        for num in nums:
            if num & res == 0:
                rst[0] ^= num
            else:
                rst[1] ^= num

        return rst

nums = [1, 2, 1, 3, 2, 5]
print(Solution().singleNumber(nums))