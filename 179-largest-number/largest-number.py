class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i] , nums[j] = nums[j] , nums[i]

        res = "".join(nums)
        if res[0] == "0":
            return "0"
        else:
            return res