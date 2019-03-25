class Solution:
    def isPopOrder(self, pushV, popV):
        if len(pushV) == 0:
            return False
        stack = []
        for i in range(len(pushV)):
            j = 0
            stack.append(pushV[i])
            i += 1
            while j < len(popV) and stack