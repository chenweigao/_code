# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(len(array)):
            temp = array[i]
            if array[i] % 2 == 1:
                j = i
                while j >= 1 and array[j - 1] % 2 == 0:
                    array[j] = array[j - 1]
                    j -= 1
                array[j] = temp
  