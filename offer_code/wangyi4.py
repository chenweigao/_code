class Solution:
    def solution(self, array):
        n = len(array)
        slide_window = 1
        for i in range(array):
            for j in range(array[0]):
                
