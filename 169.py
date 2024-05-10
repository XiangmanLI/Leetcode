class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)/2
        nums.sort()
        print(nums)

        idx = 0
        i = 0
        a = 1
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                a += 1
                i += 1
                if i+1 == len(nums):
                    if a > k:
                      idx = nums[i]
            else:
                if a > k:
                    idx = nums[i]
                    a = 0
                i+=1
        return idx
            
