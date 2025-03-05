class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        i = 0
        last_idx = 0

        while i < len(nums):

            if i <= last_idx:
                temp = i + nums[i]
                last_idx = max(last_idx , temp)
                i += 1

            else:
                return False

        return True

            

