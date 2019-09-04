class Solution:
    def find_in_array(self, alist, target) -> bool:
        """
        在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
        请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

        思路：从左下角开始找，遇到比左下角大的元素向右找，遇到比左下角小的元素向上找
        """
        row_size = len(alist)
        col_size = len(alist[0])
        row = row_size - 1
        i = row_size - 1
        j = 0

        while j < col_size and i >= 0:
            if target < alist[i][j]:
                i -= 1
            elif target > alist[i][j]:
                j += 1
            else:
                return True
        return False

    def find_in_array_binary_search(self, alist, target) -> bool:
    """
    思路二是利用二分查找的思想：
    需要遍历每一行得到最后的答案，这个操作顺便复习一下二分查找
    """
    for i in range(len(alist)):
        l = 0
        r = len(alist[i]) - 1
        while l <= r:
            mid = (l + r) // 2
            # mid = l + (r - l) // 2
            if target < alist[i][mid]:
                l = mid + 1
            elif target > alist[i][mid]:
                r = mid - 1
            else:
                return True
    return False