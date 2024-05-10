class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        a = 0
        k = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                a +=1
                i +=1
            else:
                if a >2:
                    k = a-2
                    del nums[i-k : i]
                    a = 0
                if a == 2:
                    del nums[i]
                    a = 0
                i += 1
        return len(nums)
        
