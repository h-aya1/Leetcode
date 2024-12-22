class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i + 1
        val = 0
        if len(nums) ==1 :
            return 1
        while j < len(nums):
            if nums[j - 1] < nums[j]:
                j += 1    
            else:
                i = j
                j += 1
            val = max(val , j - i)
        return val