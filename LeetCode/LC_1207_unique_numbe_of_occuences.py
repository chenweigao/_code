class Solution:
    def uniqueOccurrences(self, arr: 'List[int]') -> bool:
        values = []
        arr_dict = {}
        for n in arr:
            arr_dict[n] = arr_dict.get(n, 0) + 1
        for value in arr_dict.values():
            values.append(value)
        return len(values) == len(set(values))

import collections
class Solution2:
    def uniqueOccurrences(self, arr: 'List[int]') -> bool:
        arr_dict = collections.Counter(arr)
        return len(set(arr_dict.values())) == len(arr_dict)

arr = [1,2,2,1,1,3]
print(Solution().uniqueOccurrences(arr))
print(Solution2().uniqueOccurrences(arr))
