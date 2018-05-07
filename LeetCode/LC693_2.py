class Solution:
    def hasAlternatingBits(slef, n):
        if not n:
            return False
        n, cur = divmod(n, 2)
        # return n%2, n//2
        while n:
            if cur == n % 2:
                return False
            n, cur = divmod(n, 2)
        return True


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格）

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line)

            ret = Solution().hasAlternatingBits(n)
            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
