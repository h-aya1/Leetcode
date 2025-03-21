class Solution:
    def intToRoman(self, num: int) -> str:
        dict1 = {1 :"I", 4:"IV", 5:"V", 9:"IX" , 10:"X", 40:"XL", 50 :"L", 90:"XC", 100:"C" , 400:"CD", 500:"D" , 900:"CM", 1000:"M"}
        rom = ""
        for val , sym in sorted(dict1.items() ,reverse = True):
            while num >= val:
                rom += sym
                num -= val
        return rom