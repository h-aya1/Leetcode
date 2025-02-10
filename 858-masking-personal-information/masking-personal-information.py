class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower().split("@")
            name = s[0][0]+ "*****" +s[0][-1]
            return name + "@" + s[-1]
        else:
            sep = ['+', '-', '(', ')', ' ']
            for n in s:
                if n in sep:
                    s = s.replace(n,"")
            if len(s) == 10:
                return "***-***-" + s[-4:]
                
            return '+' + '*' * (len(s) - 10) + '-***-***-' + s[-4:]