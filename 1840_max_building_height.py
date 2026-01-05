# after solving #3796, went back and solved this
# same method, validating left and right (see #3796)
# this time, we need to optimize for memory
# as well as calculate the max height for the case where we have to go up first then back down
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n])
            
        i = 0
        m = len(restrictions)
        for j in range(1, m):
            a, b = restrictions[i][0], restrictions[j][0]
            restrictions[j][1] = min(restrictions[j][1], restrictions[i][1] + b - a)
            i = j
        
        j = m - 1
        for i in range(m-2, -1, -1):
            a, b = restrictions[i][0], restrictions[j][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[j][1] + b - a)
            j = i
        
        ans = 0
        for (a, ma), (b, mb) in pairwise(restrictions):
            ans = max(ans, ma + (mb - ma + b - a) // 2)
        return ans