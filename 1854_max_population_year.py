# i use hash map for keeping track of population changes
# then sort by year and append the changes to population
# you may not use sort, but instead exploit the year range constraint for an O(n) line sweep
# but i prefer something more general
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = {}
        for b, d in logs:
            if b not in changes:
                changes[b] = 0
            changes[b] += 1
            if d not in changes:
                changes[d] = 0
            changes[d] -= 1
        
        p = 0
        p_max = 0
        y = 0
        for k in sorted(changes.keys()):
            p += changes[k]
            if p > p_max:
                p_max = p
                y = k

        return y