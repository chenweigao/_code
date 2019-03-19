from collections import Counter

nums = [2, 2, 1, 1, 1, 2, 2]

counts = Counter(nums)

res = max(counts, key=counts.get)

print(res)