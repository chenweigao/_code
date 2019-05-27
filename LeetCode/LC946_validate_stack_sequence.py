class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:

        '''
        保持 popped 和 pushed 不变 使用辅助数组
        '''
        i = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        # print(stack, pushed, popped)
        return stack == []

        # returen i == len(poped)


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

print(Solution().validateStackSequences(pushed, popped))
