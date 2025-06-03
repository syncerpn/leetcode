# fairly easy, not hard
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        r = set([a for a in initialBoxes if status[a] == 1])
        l = set([a for a in initialBoxes if status[a] == 0])
        k = set()
        ans = 0
        while r:
            a = r.pop()
            ans += candies[a]
            for b in keys[a]:
                k.add(b)
                if b in l:
                    r.add(b)
                    l.remove(b)
            for b in containedBoxes[a]:
                if status[b] == 1 or b in k:
                    r.add(b)
                else:
                    l.add(b)
        return ans