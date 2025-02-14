class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        dict_t = Counter(t)
        required = len(dict_t)

        window_freq = defaultdict(int)
        acquired = 0

        left = 0

        solution = ( -1 , n+1)

        for right in range(n):
            char = s[right]
            window_freq[char] += 1

            if char in t and window_freq[char] == dict_t[char]:
                acquired += 1

            while required == acquired:
                
                left_char = s[left]        
                window_freq[left_char] -= 1

                if solution[1] - solution[0] > right - left:
                    solution = (left, right)

                if window_freq[left_char] < dict_t[left_char]:
                    acquired -= 1

                left += 1
        if solution[0] == -1:
            return ""
        else:
            return s[solution[0]:solution[1]+1]