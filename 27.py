class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = []
        i = 0
        c = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i+=1
        
        return len(nums)        
