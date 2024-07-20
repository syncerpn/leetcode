# optimal O(n) one-pass
# we track rolling index i of min and max element which is indexDifference away from currently considering index j
# where j always bigger than i
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        i_max, i_min = 0, 0
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            ni, nj, ni_max, ni_min = nums[i], nums[j], nums[i_max], nums[i_min]
            if ni > ni_max: i_max, ni_max = i, ni
            if ni < ni_min: i_min, ni_min = i, ni
            if abs(nj - ni_min) >= valueDifference: return [i_min, j]
            if abs(nj - ni_max) >= valueDifference: return [i_max, j]

        return [-1, -1]

# monostack was my first approach (before knowing we can solve in one-pass O(n))
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        if indexDifference >= n:
            return [-1, -1]
            
        r_max = []
        r_min = []
        for j in range(n-1, indexDifference-1, -1):
            nj = nums[j]
            if not r_max or (r_max and nj > r_max[-1][1]):
                r_max.append((j, nj))
            if not r_min or (r_min and nj < r_min[-1][1]):
                r_min.append((j, nj))
        
        j_max, nj_max = r_max.pop()
        j_min, nj_min = r_min.pop()
        for i in range(0, n-indexDifference):
            ni = nums[i]
            while r_max and j_max - indexDifference < i:
                j_max, nj_max = r_max.pop()
                
            while r_min and j_min - indexDifference < i:
                j_min, nj_min = r_min.pop()
            
            if abs(j_max - i) >= indexDifference and abs(nj_max - ni) >= valueDifference:
                return [i, j_max]
            
            if abs(j_min - i) >= indexDifference and abs(nj_min - ni) >= valueDifference:
                return [i, j_min]
        
        return [-1, -1]