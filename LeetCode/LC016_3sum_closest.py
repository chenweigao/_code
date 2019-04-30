class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:

        sum = 0
        res = float('inf')
        nums.sort()
        for i in range(len(nums)):
            front = i + 1
            back = len(nums) - 1

            while front < back:
                sum = nums[i] + nums[front] + nums[back]
                
                if sum == target:
                    return target
                elif abs(sum - target) <= abs(res - target):
                    res = sum
                if sum < target:
                    front += 1
                elif sum > target:
                    back -= 1

        return res
        


nums = [-1, 2, 1, -4]
target = 1

print(Solution().threeSumClosest(nums, target))