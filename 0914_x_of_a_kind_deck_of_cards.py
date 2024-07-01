# it becomes finding common divisor which is bigger than 1
# if exists, we can do the partition
# otherwise, return false
# reduce func is just so nice to use here
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        d = {}
        for n in deck:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        v = set(d.values())
        return reduce(gcd, v) > 1