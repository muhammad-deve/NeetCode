class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        mid = (0 + (len(merged) - 1)) // 2

        if len(merged) % 2 == 1:
            return merged[mid]
        else:
            return (merged[mid] + merged[mid + 1]) / 2