class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = nums1.copy()
        nums1.clear()
        for i in range(0,m):
            nums1.append(k[i])
        for j in range(0,n):
            nums1.append(nums2[j])
        nums1.sort()
        
        