class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        strs = strs.split()
        '''
        zip(pattern, strs): zip 对象中有两个参数对应元素的组合
        '''
        return len(set(pattern)) == len(set(strs)) == len(set(zip(pattern, strs))) and len(pattern) == len(strs)

