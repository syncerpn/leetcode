# pretty good "easy" problem that requires brainstorming
# without being too tricky
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        nk = tickets[k]
        for i, n in enumerate(tickets):
            if i <= k:
                t += min(nk, n)
            else:
                t += min(nk-1, n)
        return t