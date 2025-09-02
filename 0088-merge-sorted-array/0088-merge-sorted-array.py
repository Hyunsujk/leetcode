class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        insert = len(nums1) - 1

        while pointer2 >= 0 and pointer1 >= 0:
            if nums2[pointer2] >= nums1[pointer1]:
                nums1[insert] = nums2[pointer2]
                insert -= 1
                pointer2 -= 1
            else:
                nums1[insert], nums1[pointer1] = nums1[pointer1], nums1[insert]
                pointer1 -= 1
                insert -= 1
        
        while pointer2 >= 0:
            nums1[insert] = nums2[pointer2]
            insert -= 1
            pointer2 -= 1
        
        