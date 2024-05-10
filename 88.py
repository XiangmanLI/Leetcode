class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m-1
        q = n-1
        k = m+n-1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        while p>= 0 and q>=0:
            if nums1[p]>=nums2[q]:
                nums1[k] = nums1[p]
                p = p-1
                k = k-1
            else:
                nums1[k] = nums2[q]
                q = q-1
                k = k-1


