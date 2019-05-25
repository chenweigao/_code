class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for ch in s + t:
            res ^= ord(ch)

        return chr(res)


s = "abcd"
t = "abcde"
print(Solution().findTheDifference(s, t))


class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        print(dic)
        
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1

class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


s = "abcd"
t = "abcde"
print(Solution2().findTheDifference(s, t))