class Solution:
    def toDec(self, s) -> str:
        s = s[2:][::-1]
        dic = '0123456789ABCDEF'
        
        res = []
        for i in range(len(s)):
            res.append(dic.index(s[i]) * (16 ** i))
            
        return str(sum(res))


s = '0xC460'
print(Solution().toDec(s))
print(int(s, 16))

# while True:
#     try:
#         s = input()
#         print(Solution().toDec(s))
#     except:
#         break