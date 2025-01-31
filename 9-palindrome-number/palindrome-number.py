class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        s = str(x)  # Convert number to string
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True