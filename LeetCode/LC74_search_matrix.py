class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            _mid = matrix[mid // n][mid % n]
            if _mid == target:
                return True
            elif _mid < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


class Solution2:
    def searchMatrix(self, matrix: 'List[List[int]]', target: int) -> bool:
        for row in matrix:
            if target in row:
                return True
        return False

# matrix = [
#     [1,   3,  5,  7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 50]
# ]
# target = 3

matrix = [[1, 4], [2, 5]]
target = 2
print(Solution().searchMatrix(matrix, target))
