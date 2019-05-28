class Solution:
    def fizzBuzz(self, num: int) -> 'List[str]':
        res = []
        for n in range(1, num + 1):
            if n % 15 == 0:
                res.append("FizzBuzz")
            elif n % 5 == 0:
                res.append("Buzz")
            elif n % 3 == 0:
                res.append("Fizz")

            else:
                res.append(str(n))

        return res


class Solution2:
    def fizzBuzz(self, n: int) -> 'List[str]':
        res = []

        fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}

        for num in range(1, n + 1):

            ans_str = ""

            for k in fizz_buzz_dict.keys():
                if num % k == 0:
                    ans_str += fizz_buzz_dict[k]

            if not ans_str:
                ans_str = str(num)
            res.append(ans_str)

        return res


n = 15

print(Solution2().fizzBuzz(n))
