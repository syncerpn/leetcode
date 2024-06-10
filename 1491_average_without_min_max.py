#1. one-pass, tracking all min, max, and total
#2. simple subtract min and max from total, then take the average
def solve(salary: list) -> float:
    smin = salary[0]
    smax = salary[0]
    total = 0
    for s in salary:
        total += s
        if s > smax:
            smax = s
        if s < smin:
            smin = s
    
    return (total - smax - smin) / (len(salary) - 2)