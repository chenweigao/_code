class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.nSquare(n)
        fast = self.nSquare(self.nSquare(n))
        while slow != fast:
            slow = self.nSquare(slow)
            fast = self.nSquare(fast)
            fast = self.nSquare(fast)

        if slow == 1:
            return True
        else:
            return False


    def nSquare(self, n):
        res = 0
        while n:
            res += (n % 10)** 2
            n //= 10
        return res
    
print(Solution().isHappy(19))

class Solution2:
    def isHappy(self, n: int) -> bool:
        mem = set()

        while n not in mem:
            mem.add(n)
            n = sum(int(i)** 2 for i in str(n))
        return 1 in mem

print(Solution2().isHappy(20))
