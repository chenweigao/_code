class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                # If the number is the same as the number before, we have used it as target already, continue.
                continue

            target = -1 * nums[i]
            front = i + 1
            back = len(nums) - 1

            while front < back:
                sum = nums[front] + nums[back]
                if sum == target:
                    res.append([nums[i], nums[front], nums[back]])
                    # for we do not get repeat answers
                    while front < back and nums[front] == nums[front + 1]:
                        front += 1
                    while front < back and nums[back] == nums[back - 1]:
                        back -= 1
                    front += 1
                    back -= 1
                if sum > target:
                    back -= 1
                elif sum < target:
                    front += 1    
        return res


nums = [-1, 0, 1, 2, -1, -4]

print(Solution().threeSum(nums))
