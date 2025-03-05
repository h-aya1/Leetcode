class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count = s.count("1")
        
        zeros = len(s) - count

        return "1" * (count - 1) + "0" * zeros + "1" 
             