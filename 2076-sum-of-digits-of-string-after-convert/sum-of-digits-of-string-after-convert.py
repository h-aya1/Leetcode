class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = ""
        summ = 0
        for char in s:
            p = ord(char) - ord('a') + 1
            ans += str(p)
        while k > 0:
            summ = 0
            for n in ans:
                summ += int(n)
            ans = str(summ)
            k -= 1
        return summ