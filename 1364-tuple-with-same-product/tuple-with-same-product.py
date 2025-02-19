class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        products = defaultdict(int)
        count = 0

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):

                prod = nums[i] * nums[j]
                count += products[prod]
                products[prod] += 1

        return count * 8