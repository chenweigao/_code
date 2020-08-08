# https://leetcode-cn.com/problems/shortest-supersequence-lcci/
class Solution:
    def shortestSeq(self, big: 'List[int]', small: 'List[int]') -> 'List[int]':
        if len(big) < len(small):
            return []
        left, right = 0, 0  
        # start, res 用于保存最优解
        # start 是最终结果的开始位置，res 是最终结果的长度
        start = 0
        res = len(big) + 1
        
        small_dict = dict()
        for num in small:
            small_dict[num] = small_dict.get(num, 0) + 1
        
        window = dict()
        match = 0
        while right < len(big):
            # 开始滑动
            # 先看一下右边元素在没在 small_dict 中
            if big[right] in small_dict:
                # 如果在的话，放进一个字典中
                window[big[right]] = window.get(big[right], 0) + 1
                # 判断一下，如果数量满足的话
                if small_dict.get(big[right]) == window.get(big[right]):
                    # 数量满足的话说明这个数已经满足了
                    match += 1

            # 否则 继续滑动
            right += 1
            # 判断一下是不是满足了退出条件
            while match == sum(small_dict.values()):
                # 更新窗口大小
                if right - left < res:
                    # 更新窗口
                    start = left
                    res = right- left
                # 现在需要做的就是更新左边的指针
                if big[left] in small_dict:
                    # 减少滑动窗口，看 match 是否减少，减少的话就退出，未减少的话
                    window[big[left]] = window.get(big[left], 0) - 1
                    if window.get(big[left], 0) < small_dict.get(big[left], 0):
                        match -= 1
                left += 1
        
        return [] if res > len(big) + 1 else [start, start + res - 1]



big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
small = [1,5,9]

print(Solution().shortestSeq(big, small))

big2 = [1]
small2 = [1,2]

print(Solution().shortestSeq(big2,small2))