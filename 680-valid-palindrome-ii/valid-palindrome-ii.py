class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        if s == s[::-1]:
            return True
        
        while l <= r and r > 0:

            if s[l] != s[r]:
                out_l = s[l + 1: r + 1]
                out_r = s[l:r]

                if out_l == out_l[::-1] or out_r == out_r[::-1]:
                    return True
                else:
                    return False

            l += 1
            r -= 1
        return True