class Solution:
    def solution(self, array):
        res = 0
        n = len(array)
        for i in range(n):
            if array[i] > array[n - i - 1]:
                res += array[i]
                del array[i]