class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 == 0:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2
        else:
            return nums[n // 2] * 2 / 2

class Solution2:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(num2, nums1)
        k = (n1 + n2 + 1) // 2

        left = 0
        right = n1

        while left < right:
            m1 = left + (right - left) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1

nums1 = [-1, 1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10, 12, 14, 16]

print(Solution().findMedianSortedArrays(nums1, nums2))
