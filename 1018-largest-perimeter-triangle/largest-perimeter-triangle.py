class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        c = len(nums) - 1
        b = c - 1
        a = b - 1
        peri = 0 

        while a >= 0:

            if (nums[a] + nums[b]) > nums[c]:

                peri = max(peri , nums[a] + nums[b] + nums[c])
                break

            a -= 1
            b -= 1
            c -= 1

        return peri


