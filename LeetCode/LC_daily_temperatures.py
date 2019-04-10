class Solution:
    # def dailyTemperatures(self, T):
    #     n = len(T)
    #     res = [0 for _ in range(n)]

    #     stack = []
    #     for i, t in enumerate(T):
    #         while stack and T[stack[-1]] < t:
    #             cur = stack.pop()
    #             print("cur: ", cur)
    #             res[cur] = i - cur
    #             print("res[cur]: ", res[cur])
    #         stack.append(i)
    #     return res
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0 for _ in range((n))]
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res                

        

T = [73, 74, 75, 71, 69, 72, 76, 73]

n = len(T)
res = [0 for _ in T]
stack =[]

for i in range(n - 1, -1, -1):
    while stack and T[i] >= T[stack[-1]]:
        stack.pop()
    if stack:
        res[i] = stack[-1] - i
    stack.append(i)
