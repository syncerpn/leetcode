# greedily schedule for odd days first, then remaining for even days
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas) // 4
        p, q = (n + 1) // 2, n // 2
        return sum(pizzas[-1-i] for i in range(p)) + sum(pizzas[-2-p-i*2] for i in range(q))