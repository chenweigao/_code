class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        stack = []
        for i in range(n):
            stack.append('(')
            