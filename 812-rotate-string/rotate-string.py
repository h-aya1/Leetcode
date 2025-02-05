class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ns = s + s
        if goal in ns:
            return True
        
        return False