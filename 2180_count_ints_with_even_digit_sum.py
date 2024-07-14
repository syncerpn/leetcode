# optimized O(lgn)
# explanation is:
# for every pair of adjacent nums
# digit sum of one is even and of another is odd
# this pairity is swapped when there is transition 9 -> 0
# also, the number of even digit sum numbers is half or half-1 of num
# this depends on the last element, which is num itself
# so, all we need to check is digit sum of num
class Solution:
    def countEven(self, num: int) -> int:
        s = 0
        n = num
        while n:
            s += n % 10
            n //= 10
        
        return (num - (s & 1)) // 2