class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        dic = {}
        res = []

        for num in nums1:
            dic[num] = dic.get(num, 0) + 1
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(Solution().intersect(nums1, nums2))


class Solution2:
    '''
    if the given array is already sorted, give the solution
    '''

    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if not nums1 or not nums2:
            return []

        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res


nums1 = [1, 2, 2, 3, 1]
nums2 = [2, 2, 2, 3, 4, 5]
print(Solution2().intersect(nums1, nums2))
