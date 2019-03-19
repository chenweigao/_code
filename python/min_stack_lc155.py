class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minst = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.minst == []:
            self.minst.append(x)
        elif x <= self.minst[-1]:
            self.minst.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        # return self.stack.pop()
        p = self.stack.pop()
        if self.minst:
            if self.minst[-1] == p:
                self.minst.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # return sorted(self.stack)[0]
        if self.minst:
            return self.minst[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(3)
obj.push(-1)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
