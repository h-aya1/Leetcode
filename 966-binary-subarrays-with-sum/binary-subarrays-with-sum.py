class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        subs = defaultdict(int)
        subs[0] = 1

        preSum = 0
        count = 0

        for num in nums:

            preSum += num
            count += subs[preSum - goal] 
            subs[preSum] += 1
        return count