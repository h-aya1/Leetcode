class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 0
        runningSum = []

        for j in range(len(nums)):
            runningSum.append(sum(nums[i:j+1]))
        
        return runningSum