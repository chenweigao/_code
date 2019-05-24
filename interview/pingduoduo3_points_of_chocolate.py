class Solution:
    def chocolate(self, h: 'List', w: 'List'):
        '''
        h: 表示小朋友  2 2 3

        w: 表示巧克力  1 3
        '''
        res = 0
        h = sorted(h)
        w = sorted(w)
        
        i, j = 0, 0

        while i < len(h) and j < len(w):
            if h[i] > w[j]:
                j += 1
            else:
                i += 1
                j += 1
                res += 1

        return res

while True:
    try:
        n = int(input())
        h = list(map(int, input().split()))
        m = int(input())
        w = list(map(int, input().split()))
        print(Solution().chocolate(h, w))
    except:
        break


# h = [2, 2, 3]
# w = [3, 1]

# print(Solution().chocolate(h, w))