from collections import defaultdict
class Solution:

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        ans = []
        for path in paths:
            r , *n = path.split()

            for c in n:
                fn , cont = c.split("(")
                dict1[cont].append(r+"/"+fn)
        for cont in dict1:
            if len(dict1[cont]) > 1:
                ans.append(dict1[cont])
        return ans