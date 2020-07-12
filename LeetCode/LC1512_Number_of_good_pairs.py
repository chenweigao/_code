# 该题目要求找到相等的数，然后再判断其下标大小关系
# 先尝试用暴力方法求解，理解一下题目

class Solution:
    def numIdenticalPairs(self, nums: 'List[int]') -> int:
        if len(set(nums)) == len(nums):
            return 0
        res = 0
        for i, _ in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    res += 1
                    j += 1
                else:
                    j += 1
        return res

nums = [1,2,3,1,1,3]
print(Solution().numIdenticalPairs(nums))

nums2 = [1,1,1,1]
print(Solution().numIdenticalPairs(nums2))


# 上面的方法很简单，很快就可以通过，现在思考一下有无更快的方法
# hash map是否可行呢

class Solution2:
    def numIdenticalPairs(self, nums: 'List[int]') -> int:
        # 先构建 hash map
        res = 0
        hash_map = dict()
        for num in nums:
            res += hash_map.get(num, 0)
            hash_map[num] = hash_map.get(num, 0) + 1
        # hash_map = {1: 3, 2: 1, 3: 2}
        # 这是构造了一个hash_map
        return res


print(Solution2().numIdenticalPairs(nums))