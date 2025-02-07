class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        num = 0
        pre = 0
        for n in reversed(s):
            curr = dict1[n]
            if curr < pre:
                num -= curr
            else:
                num += curr
            pre = curr
        return num