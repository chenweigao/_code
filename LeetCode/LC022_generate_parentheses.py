class Solution:
    def generateParenthesis(self, n: int) -> 'List[str]':
        def generate(res=[]):
            if len(res) == 2 * n:
                if vaild(res):
                    ans.append(''.join(res))
            else:
                res.append('(')
                generate(res)
                res.pop()
                res.append(')')
                generate(res)
                res.pop()
        def vaild(res):
            bal = 0
            for ch in res:
                if ch == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        
        ans = []
        generate()
        return ans