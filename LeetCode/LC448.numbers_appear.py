class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
            print(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

    def findDisappearedNumbers2(self, nums):
        size = len(nums)
        nset = set(nums)
        return [n for n in range(1, size + 1) if n not in nset]


nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(Solution().findDisappearedNumbers2(nums))
