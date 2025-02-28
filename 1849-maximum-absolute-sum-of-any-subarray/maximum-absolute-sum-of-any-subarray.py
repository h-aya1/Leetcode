class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        max_sumP = curr_sumP = max_sumN = curr_sumN = nums[0]

        for i in range(1 ,len(nums)):

            curr_sumP = max(nums[i] , curr_sumP + nums[i])
            max_sumP = max(max_sumP , curr_sumP)

        for i in range(1 ,len(nums)):

            curr_sumN = min(nums[i] , curr_sumN + nums[i])
            max_sumN = min(max_sumN , curr_sumN)
        print(max_sumN)
        print(max_sumP)

        return max(abs(max_sumN) , max_sumP)
