# simulate it
# but this is not the optimal way
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        d = list(map(int, list(s)))
        while len(d) > 2:
            for i in range(len(d)-1):
                d[i] = (d[i] + d[i+1]) % 10
            d.pop()
        
        return d[0] == d[1]