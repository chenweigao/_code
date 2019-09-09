#coding=utf-8
import sys 
class  Solution:
    def solution(self, x, y):
        sum_x_y = self.rev(x) + self.rev(y)
        return self.rev(sum_x_y)
    def rev(self, x):
        res = 0
        while x != 0:
            res = x % 10 + 10 * res
            x = x // 10
        return res

# line_str = input().split(' ')

# x, y = [int(_) for _ in line_str]
# print(Solution().solution(x, y))