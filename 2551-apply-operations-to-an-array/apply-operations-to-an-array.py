class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

            i += 1
        x = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[x], nums[j] = nums[j], nums[x]
                x += 1
        return nums