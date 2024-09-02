# sort by dps
# just took a few trials to come up with the correct solution
class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        meta = sorted(range(len(damage)), key=lambda i: damage[i] / (ceil(health[i] / power)), reverse=True)
        t = sum(damage)
        ans = 0
        for i in meta:
            ans += t * int(ceil(health[i] / power))
            t -= damage[i]
        return ans