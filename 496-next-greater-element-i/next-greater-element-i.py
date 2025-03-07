class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        ng = defaultdict(lambda: -1)
        ans = []

        for num in nums2:

            while stack and num > stack[-1]:

                anothNum = stack.pop()
                ng[anothNum] = num

            stack.append(num)
            
        for num in nums1:
            ans.append(ng[num])

        return ans


