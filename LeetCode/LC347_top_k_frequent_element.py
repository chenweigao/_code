import collections


class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        res = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        return [_[0] for _ in res[:k]]


class Solution2:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]':
        count = collections.Counter(nums)
        res = count.most_common(k)

        return [_[0] for _ in res]


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(Solution2().topKFrequent(nums, k))
