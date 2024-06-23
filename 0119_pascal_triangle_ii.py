# return one row instead of the whole triangle
# redundant code can be removed
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        for i in range(1, rowIndex+1):
            t = [1]
            for j in range(1, i):
                t.append(r[j] + r[j-1])
            t.append(1)
            r = t
        
        return r

# use pure math and binomial coefficient
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [1]
        p = 1
        for i in range(1, rowIndex+1):
            n = p * (rowIndex - i + 1) // i
            r.append(n)
            p = n
        return r