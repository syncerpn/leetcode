#1. using math
def solve(numRows: int) -> list:
    result = [[1]]
    for i in range(1, numRows):
        r = result[i-1]
        t = [1]
        for j in range(1, i):
            t.append(r[j] + r[j-1])
        t.append(1)
        result.append(t)
    
    return result