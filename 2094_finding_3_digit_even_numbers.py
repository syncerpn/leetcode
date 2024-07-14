# save lots of time (sorting, permutation, etc.)
# if we check every 3-digit even numbers
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = {i:0 for i in range(10)}
        for d in digits:
            c[d] += 1

        r = []
        for i in range(1, 10):
            f = {i:1}
            for j in range(10):
                if j not in f:
                    f[j] = 0
                f[j] += 1
                for k in range(0, 10, 2):
                    if k not in f:
                        f[k] = 0
                    f[k] += 1
                    if f[i] <= c[i] and f[j] <= c[j] and f[k] <= c[k]:
                        r.append(i*100+j*10+k)
                    f[k] -= 1
                f[j] -= 1
        
        return r