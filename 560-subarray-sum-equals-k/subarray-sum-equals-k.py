class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        preSum = 0
        count = 0
        i = 0
        preCount = {0: 1} 

        for num in nums:
            preSum += num
        
            if preSum - k in preCount:
                count += preCount[preSum - k]
            
            
            preCount[preSum] = preCount.get(preSum, 0) + 1


        return count
        