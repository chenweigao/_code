class Solution:
    def solution(self, dic, total):
        sort_dic = sorted(dic.items(), key=lambda x: x[1] * x[0], reverse=True)

        remain = total
        profit = 0
        for count, delta in sort_dic:
            if delta > 0 and remain >= count:
                    remain = remain - count
                    profit = count * delta + profit
            else:
                continue
        return profit


        # return dic


# dic = {
#     100: -0.05,
#     320: 0.05,
#     120: 0,
#     20: 0.03,
#     80: 0.04
# }
# total = 500

total = int(input())
n = int(input())
dic = {}
for i in range(n):
    k, v = [float(_) for _ in input().split(',')]
    dic[k] = v
print(dic)

res = Solution().solution(dic, total)

print("%.4f" % res)