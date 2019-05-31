class Solution:
    def partitionLabels(self, S: str) -> 'List[int]':
        dic = {}
        n = len(S)
        for i in range(n):
            dic[S[i]] = i

        start, end = 0, 0
        res = []
        for i in range(n):
            end = max(end, dic[S[i]])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res

S = 'ababcbacadefegdehijhklij'

print(Solution().partitionLabels(S))