# fairly easy with stack
# why tagged as hard?
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for a in nums:
            if not s:
                s.append(a)
                continue
            while s:
                b = s.pop()
                d = math.gcd(b, a)
                if d == 1:
                    s.append(b)
                    break
                a = b // d * a
            s.append(a)
        return s