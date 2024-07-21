# O(qn) time
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for a, b, r in queries:
            n = 0
            for x, y in points:
                if (x-a)*(x-a) + (y-b)*(y-b) <= r*r:
                    n += 1
            
            ans.append(n)
        return ans

# could be improved by sorting points
# then use binary search to filter points with abs(x-a) and (y-b) within range [0,r]
# though i hate binary search