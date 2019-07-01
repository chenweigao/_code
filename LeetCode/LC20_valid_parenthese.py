'''
遇到左括号则入栈，遇到右括号判断是否与栈顶元素匹配，直到最后判断栈是否为空
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                # for the case "]"
                if stack == []:
                    return False
                if ch == ')' and stack[-1] != '(':
                    return False
                if ch == ']' and stack[-1] != '[':
                    return False
                if ch == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return stack == []
print(Solution().isValid("]"))


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"]":"[", "}":"{", ")":"("}

        for ch in s:
            if ch in mapping.keys(): # 右括号，进行判断
                if stack == []:
                    return False
                if stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch) # 左括号，入栈
        return stack == []

