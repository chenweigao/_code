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

class Solution2:
    def jump(self, nums):
        count = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                count += 1
                end = farthest
        return count
