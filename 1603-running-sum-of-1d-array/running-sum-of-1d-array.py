class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        runningSum = []
        preSum = 0
        
        for j in range(len(nums)):
            preSum += nums[j]
            runningSum.append(preSum)
        return runningSum