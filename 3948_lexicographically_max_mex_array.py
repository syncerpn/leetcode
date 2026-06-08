# was not that hard yet failed to solve it on time
# the idea is to choose a shortest prefix that has the same mex as the whole array
# to do so, we keep track of the elements in the whole array first
# then loop this until the array is empty
# 1. find the mex of the remaining array
# 2. remove elements one by one until the mex is achieved
# 3. add the mex to ans
# 4. go back to 1
class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for a in nums:
            d[a] += 1
        
        ans = []
        i, n = 0, len(nums)
        
        while i < n:
            b = 0
            while d[b]:
                b += 1
            
            if b == 0:
                while i < n:
                    ans.append(0)
                    i += 1
                break
            
            s = set(range(b))
            while s:
                a = nums[i]
                d[a] -= 1
                if a in s:
                    s.remove(a)
                i += 1
            ans.append(b)
        
        return ans

# implemented as bit array
class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for a in nums:
            d[a] += 1
        
        ans = []
        i, n = 0, len(nums)
        
        while i < n:
            b = 0
            while d[b]:
                b += 1
            
            if b == 0:
                while i < n:
                    ans.append(0)
                    i += 1
                break
            
            s = [True] * b
            k = b
            while k:
                a = nums[i]
                d[a] -= 1
                if a < b and s[a]:
                    s[a] = False
                    k -= 1
                i += 1
            ans.append(b)
        
        return ans