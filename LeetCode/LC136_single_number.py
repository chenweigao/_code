class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = {}
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        return hash_table.popitem()[0]


class Solution2:
    def singleNumber(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)


class Solution3:
    def singleNumber(self, nums) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a

nums = [4, 1, 2, 1, 2]

res = Solution().singleNumber(nums)
res2 = Solution3().singleNumber(nums)
