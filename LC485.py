class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cnt = 0, 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 0
        return ans
def stringToIntegerList(input):
    import json
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().findMaxConsecutiveOnes(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()