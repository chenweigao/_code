class Solution:
    def big_int_multi(self, str1, str2):
        c = [0 for _ in range(max(len(str1), len(str2)))]
        res = [0 for _ in range(len(str1) + len(str2))]
        for i in range(len(str1) - 1, -1, -1):
            x = int(str1[i])
            for j in range(len(str2) - 1, -1, -1):
                y = int(str2[j])
                res[i + j] += (x * y + res[i + j + 1]) // 10
                res[i + j + 1] = (x * y + res[i + j + 1]) % 10

        s = ''
        for i in range(len(res)):
            if i == 0 and res[i] == 0:
                continue
            s += str(res[i])
        
        return s

a = "72106547548473106236"
b = "982161082972751393"
print(Solution().big_int_multi(a, b))

# while True:
#     try:
#         s = input()
#         while not s:
#             break
#         a, b = s.split()

#         print(Solution().big_int_multi(a, b))

#     except:
#         break