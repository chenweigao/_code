from builtins import input


class Solution:
    def solution(self, ip1, ip2, dns):
        ip1 = [int(_) for _ in ip1.split('.')]
        ip2 = [int(_) for _ in ip2.split('.')]

        dns = [int(_) for _ in dns.split('.')]
        res = []
        is_same = 1
        for i in range(4):
            if ip1[i] & dns[i] == ip2[i] & dns[i]:
                res.append(ip1[i] & dns[i])
            else:
                is_same = 0
                res.append(ip1[i] & dns[i])
        ans = ''
        for i in res:
            ans = ans + str(i) + '.'
        ans = ans[:-1]
        return is_same, ans

while True:
    try:
        ip1, ip2, dns = input().split()
        is_same, ans = Solution().solution(ip1, ip2, dns)
        print(is_same, ans)
    except:
        break

# ip1 = '192.168.1.1'
# ip2 = '192.168.2.1'
# dns = '255.255.255.0'
# print(Solution().solution(ip1, ip2, dns))
