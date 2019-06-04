class Solution:
    def anagramMappings(self, A, B):
        res = []

        dic = {}

        for i in range(len(B)):
            dic[B[i]] = i

        for num in A:
            res.append(dic[num])
        return res


A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

print(Solution().anagramMappings(A, B))
