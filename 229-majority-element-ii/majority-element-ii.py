class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        nums = Counter(nums)
        for num , count in nums.items():
            if count > (n/3):
                ans.append(num)
        return ans