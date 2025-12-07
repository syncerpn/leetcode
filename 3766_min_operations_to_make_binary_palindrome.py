# fair
class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        def is_binary_palindrome(a):
            b = bin(a)[2:]
            for i in range(len(b) // 2):
                if b[i] != b[~i]:
                    return False
            return True
        mi, ma = min(nums), max(nums)
        while not is_binary_palindrome(mi):
            mi -= 1
        
        while not is_binary_palindrome(ma):
            ma += 1
        
        v = []
        for a in range(mi, ma+1):
            if is_binary_palindrome(a):
                v.append(a)
        
        m = len(v)
        ans = []
        for a in nums:
            i = bisect.bisect(v, a)
            d = a - v[i-1]
            if i < m:
                d = min(v[i] - a, d)
            ans.append(d)
        return ans