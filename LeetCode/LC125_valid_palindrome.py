class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True

s = "A man, a plan, a canal: Panama"

print(Solution().isPalindrome(s))

import string
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.lower()
        s = s.replace(' ', '')
        return (s == s[::-1])



s = "A man, a plan, a canal: Panama"

print(Solution2().isPalindrome(s))


class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(s.isalnum(), s.lower()))
        return (s == s[::-1])

class Solution4:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^0-9a-z]', '', s.lower())
        return (s == s[::-1])