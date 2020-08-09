#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> bool:
        # row
        import collections
        rows = [{} for i in range(len(board))]
        cols = [{} for j in range(len(board[0]))]
        boxes = [{} for n in range(9)]  # 一共 9 个 box
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 行是否存在重复，拿出每一行的数
                num = board[i][j]
                if num != '.':
                    # 先建 hash table
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    # 判断处于哪个 box 中，先要i算 box 的索引
                    box_index = j // 3 + (i // 3) * 3
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    # hash table 建立完成，现在开始判断
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

# @lc code=end