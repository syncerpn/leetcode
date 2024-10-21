# greedy
# candidate triplets should be those with at least one element equal to its target equivalence
# and two other must be smaller or equal to their target equivalences
# also with early stopping to make it faster
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target
        ans = [False, False, False]
        for a, b, c in triplets:
            if a <= ta and b <= tb and c <= tc:
                if a == ta: ans[0] = True
                if b == tb: ans[1] = True
                if c == tc: ans[2] = True
                if all(ans):
                    return True
        return False