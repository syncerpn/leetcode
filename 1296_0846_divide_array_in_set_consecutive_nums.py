#1. need to count first
#2. as forming sets, recount the remaining
def solve(nums: list, k: int) -> bool:
    counter = {}
    for i in nums:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
    
    for i in sorted(counter.keys()):
        n = counter[i]
        if n == 0:
            continue
        for j in range(1,k):
            if i+j not in counter:
                return False
            if counter[i+j] < n:
                return False
            counter[i+j] -= counter[i]        
    return True