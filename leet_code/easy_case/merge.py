class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if nums2[-1] <= nums1[0]:
            nums1 = nusm2 + nums1
        else if num2[0] >= nums1[-1]:
            nums1 = nums1.extend(nusm2)
                    
        for i in range(0,m+n):
                    
                
