class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 for _ in s] for i in s]
        
        return dp


print(SolutionDP().longestPalindrome('abc'))