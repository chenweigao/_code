from itertools import combinations
class Solution:
    def get_all_combinations(self, array, k):
        count = 0
        for _ in combinations(array, 3):
            if sum(_) < k:
                count += 1
        return count
# array = [-2, 0, 1, 2, 3, 6]
# k = 2

m = input()
line = input().split()

k = int(input())
array = [int(_) for _ in line]
print(Solution().get_all_combinations(array, k))