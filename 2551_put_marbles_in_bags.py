# could not solve it myself though
# but the solution is so short and concise
# i decided to look at it more closely
# the thing is, when we split the marbles at some point i
# weights[i] and weights[i+1] contribute to the cost
# and the logic is, we want to cut k highest points to maximize the cost
# as well as k lowest points to minimize the cost
# so it basically converges to a simple sorting problem
# one edge case to handle here is k == 1
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        pair_sums = []
        for i in range(len(weights) - 1):
            pair_sums.append(weights[i] + weights[i + 1])
        
        pair_sums.sort()
        
        min_score = sum(pair_sums[:k-1])
        max_score = sum(pair_sums[-(k-1):])
        
        return max_score - min_score
        