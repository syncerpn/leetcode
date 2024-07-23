# O(len(target))
# optimal one i think, lol
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        ans = []
        for t in target:
            ans += (t-i-1) * ["Push", "Pop"] + ["Push"]
            i = t
        return ans