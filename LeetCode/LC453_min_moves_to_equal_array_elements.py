class Solution:
    def minMoves(self, nums: 'List[int]') -> int:
        return sum(nums) - len(nums) * min(nums)
        # 一次移动 n-1 个元素加 1, 等价于将 1 个元素减 1