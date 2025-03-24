class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        unfairness = float('inf')

        def backtrack(idx):

            nonlocal unfairness

            if idx == len(cookies):

                unfairness = min(unfairness , max(child))
                return

            for i in range(k):

                child[i] += cookies[idx]

                if unfairness > child[i]:
                    backtrack(idx + 1)

                child[i] -= cookies[idx]

        backtrack(0)

        return unfairness