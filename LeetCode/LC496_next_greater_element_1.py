class Solution:
    def nextGreaterElement(self, find_nums, nums):
        # [4, 1, 2]
        # [1, 3, 4, 2]
        # [-1, 3, -1]

        stack = []
        dic = {}

        for num in nums:
            while stack != [] and stack[-1] < num:
                # 当栈顶元素小于 num 时，在字典中添加
                # 栈顶元素：num 表示栈顶元素的 next greater element 是 num
                dic[stack[-1]] = num
                stack.pop()
            stack.append(num)
            # stack 在上述例子中的顺序变化为：[1] -> [3] -> [4] -> [4, 2]
            # dic 为 {1: 3, 3: 4}

        res = []
        
        for find_num in find_nums:
            res.append(dic.get(find_num, -1))
        return res



find_nums = [4, 1, 2]
nums = [1, 3, 4, 2]
print(Solution().nextGreaterElement(find_nums, nums))