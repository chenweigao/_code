import collections


class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        # dic = {}

        # for num in set(nums):
        #     dic[num] = nums.count(num)
        # for k, v in dic.items():
        #     if v > len(nums) / 2:
        #         return k

        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        # for k, v in dic.items():
        #     if v > len(nums) / 2:
        #         return k

        stack = []

        for num in nums:
            if stack == [] or stack[-1] == num:
                stack.append(num)
            else:
                stack.pop()
        return stack[-1]


class Solution2:
    def majorityElement(self, nums: 'List[int]') -> int:
        counts = collections.Counter(nums)
        return max(counts, key=counts.get)


nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution2().majorityElement(nums))
