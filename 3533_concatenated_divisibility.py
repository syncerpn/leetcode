# pure backtrack resulted in tle
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)
        s = [a % k for a in nums]
        m = [len(str(a)) for a in nums]
        ans = []
        v = set()

        def backtrack(r, p):
            if p == 0:
                return r == 0
            
            for i in range(n):
                if i in v:
                    continue
                
                v.add(i)
                ans.append(nums[i])

                q = p - m[i]

                if backtrack((r + s[i] * (10 ** q)) % k, q):
                    return True
                
                v.remove(i)
                ans.pop()

            return False
        
        backtrack(0, sum(m))
        return ans
        
# backtrack with dp
# dp with bitmask is the key
class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n = len(nums)
        s = [a % k for a in nums]
        m = [len(str(a)) for a in nums]
        ans = []

        @functools.cache
        def backtrack(r, p, v):
            if p == 0:
                return r == 0
            
            for i in range(n):
                if (v >> i) & 1:
                    continue
                
                v |= (1 << i)
                ans.append(nums[i])

                q = p - m[i]

                if backtrack((r + s[i] * (10 ** q)) % k, q, v):
                    return True
                
                v ^= (1 << i)
                ans.pop()

            return False
        
        backtrack(0, sum(m), 0)
        return ans