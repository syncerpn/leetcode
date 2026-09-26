# suprisingly easy for a 2100-rated question lol
# simply precompute all the palindromes
# then binary search to find out the closest one
# dont forget parity check because increment is 2 then you cant change odd to even or vice versa
P = [[], []]
for n in range(1, 6):
    for i in range(10 ** (n - 1), 10 ** n):
        #even
        k = i
        j = 0
        while k:
            j = j * 10 + k % 10
            k = k // 10
        d = i * (10 ** n) + j
        P[d % 2].append(d)

        #odd
        k = i // 10
        j = 0
        while k:
            j = j * 10 + k % 10
            k = k // 10
        d = i * (10 ** (n - 1)) + j
        P[d % 2].append(d)

P[0].sort()
P[1].sort()

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for a in nums:
            p = a % 2
            i = bisect.bisect_right(P[p], a)
            l, r = P[p][i-1], P[p][i]
            ans += min((a - l) // 2, (r - a) // 2)
        return ans