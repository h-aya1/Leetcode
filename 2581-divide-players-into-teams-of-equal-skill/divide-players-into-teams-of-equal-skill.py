class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        if len(skill) == 2:
            return skill[0] * skill[1]

        i = 0 
        j = len(skill) - 1
        ans = 0
        tot = skill[i] + skill[j]

        while i < j:

            if skill[i] + skill[j] != tot:
                return -1
            ans += (skill[i] * skill[j])

            i += 1
            j -= 1
            
        return ans