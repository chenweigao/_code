class Solution:
    def max_profit(self, array):
        if not array:
            return 0
        res = 0
        for i in range(len(array) - 1):
            temp = array[i + 1] - array[i]
            if temp > 0:
                res += temp
        return res

array = [7, 1, 5,6,3,4]

n = input()
line = input().strip()
string = line.split()
array = [int(_) for _ in string]
print(Solution().max_profit(array))