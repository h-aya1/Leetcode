class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        reminds = defaultdict(int)  
        reminds[0] = 1 
        
        preSum = 0
        count = 0  

        for num in nums:

            preSum += num 
            remainder = preSum % k  

            if remainder < 0:
                remainder += k  

            count += reminds[remainder]
            reminds[remainder] += 1  

        return count