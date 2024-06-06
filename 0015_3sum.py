#1. divide into negatives, zeros, and positives
#2. try matching them with possible cases: 3 zeros, at least one zero, two negs one pos, and two poss one neg
#3. using set for faster search
def solve(nums: list) -> list:
    if len(nums) < 3:
        return []
    
    p = []
    n = []
    z = []
    results = set()

    for i in nums:
        if i > 0:
            p += [i]
        elif i == 0:
            z += [i]
        else:
            n += [i]
    
    N, P = set(n), set(p)

    if len(z) >= 3:
        results.add((0, 0, 0))
    
    if len(z) > 0:
        for pi in p:
            if -pi in N:
                results.add((-pi, 0, pi))
    
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            if -(p[i] + p[j]) in N:
                results.add(tuple(sorted([-p[i] - p[j], p[i], p[j]])))
    
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if -(n[i] + n[j]) in P:
                results.add(tuple(sorted([n[i], n[j], -n[i] - n[j]])))
    
    return results