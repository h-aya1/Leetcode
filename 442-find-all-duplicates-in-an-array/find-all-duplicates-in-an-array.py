class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        nums = Counter(nums)
        for val , count in nums.items():
            if count > 1:
                ans.append(val)
        return ans