class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        # new = sorted(roman_dic.items(), key=lambda item: item[0], reverse=True)
        # print(dict(roman_dic))
        res = ''
        for key, value in roman_dic.items():
            res += (num // key) * value
            num %= key
        return res

test_nums = [3, 4, 9, 58, 1994]

for num in test_nums:
    print(Solution().intToRoman(num)) 
