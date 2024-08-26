# brute force solution lol
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def almost_equal(i, j):
            ni = len(i)
            nj = len(j)
            if ni > nj:
                j = "0" * (ni - nj) + j
            elif nj > ni:
                i = "0" * (nj - ni) + i
            d = []
            for ci, cj in zip(i, j):
                if ci != cj:
                    d.append((ci, cj))
            
            if len(d) == 0:
                return True
            if len(d) == 2:
                if d[0][1] == d[1][0] and d[0][0] == d[1][1]:
                    return True
            return False
        
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if almost_equal(str(nums[i]), str(nums[j])):
                    ans += 1
        return ans