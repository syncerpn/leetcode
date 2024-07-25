# nothing special
# it is just brute force with backtracking
# here i implemented the backtracking simply by generate all possible topping costs
# and sort them for early stopping
# we could also make use of dp for faster generation of the cost array
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def get_topping_cost(i):
            t = 0
            for c in toppingCosts:
                t += (i % 3) * c
                i //= 3
            return t
        
        T = sorted([get_topping_cost(i) for i in range(3 ** len(toppingCosts))])

        ans = baseCosts[0]
        for b in baseCosts:
            for t in T:
                s = b + t
                if s == target:
                    return target
                if abs(target - s) < abs(target - ans):
                    ans = s
                elif abs(target - s) == abs(target - ans):
                    ans = min(ans, s)
                elif s > target:
                    break

        return ans