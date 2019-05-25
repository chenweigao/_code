from builtins import input


class Soluiton:
    def primeFactors(self, num):
        res = []
        for i in range(2, num // 2 + 1):
            while num % i == 0:
                res.append(i)
                num //= i
        if len(res) == 0:
            res.append(num)
        return res

# num = 180


# print(Soluiton().primeFactors(num))
while True:
    try:
        num = int(input())
        res = Soluiton().primeFactors(num)
        for i in res:
            print(i, end=" ")
    except:
        break
