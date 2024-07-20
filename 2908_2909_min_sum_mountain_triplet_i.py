class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        # first pass
        # build monostack of smallest from right to left
        # stack elements are of (index, value) form
        r = []
        for i, k in enumerate(nums[::-1]):
            if r and r[-1][1] <= k:
                continue
            r.append((n-1-i, k))
        
        # second pass
        i = 0
        k, nk = r.pop()
        res = -1
        for j in range(1, n-1):
            ni, nj = nums[i], nums[j]
            
            # withdraw smallest right with index > j
            while k <= j:
                if not r:
                    return r
                k, nk = r.pop()
            
            # calculate result if the triplet satisfies the conditions
            if nj > ni and nj > nk:
                if res == -1 or res > ni + nj + nk:
                    res = ni + nj + nk

            # keep track of smallest left  
            if nj < ni:
                i = j
        
        return res