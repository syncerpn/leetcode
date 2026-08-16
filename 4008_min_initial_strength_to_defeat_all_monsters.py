# going backward, calculating the min remaining strength
# as long as the boost alone can defeat the monster, remaining should stay 0
# starting from when this is not the case, just accumulate the monsters' strength
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)
        B = [0] * (n + 1)
        
        for l, r, v in boosts:
            B[l] += v
            B[r+1] -= v
        
        for i in range(1, n+1):
            B[i] += B[i-1]
        
        ans = 0
        f = False
        for i in range(n-1, -1, -1):
            if not f:
                if B[i] < monsters[i]:
                    f = True
                    ans = monsters[i] - B[i]
            else:
                ans += monsters[i]
        return ans