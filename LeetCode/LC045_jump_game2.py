class Solution:
    def jump(self, nums):
        left, right = 0, nums[0]
        n = len(nums)
        count = 1

        if n <= 1:
            return 0

        while right < n - 1:
            count += 1
            temp = max(nums[i] + i for i in range(left + 1, right + 1))
            left, right = right, temp
        return count

arr = [2, 3, 1, 1, 4]
print(Solution().jump(arr))