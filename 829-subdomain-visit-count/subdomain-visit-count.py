class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dom = defaultdict(int)

        for doms in cpdomains:
            rep , d = doms.split()
            rep = int(rep)
            subs = d.split(".")

            for i in range(len(subs)):
                sub = ".".join(subs[i:])
                dom[sub] += rep

        ans = []
        for domain , repo in dom.items():
            ans.append(str(repo)+ " " + domain)
        return ans