# was overthinking on this one
# oh, actually not
# this is somewhat "similar to segmented tree"
# maybe like linked-list??
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [(1, m)]
        ans = []
        for q in queries:
            i = 0
            j = 0
            while j < len(P):
                a, b = P[j]
                if a <= q <= b:
                    ans.append(i + q - a)
                    if a == b:
                        P.pop(j)
                    elif a == q:
                        P[j] = (a+1, b)
                    elif b == q:
                        P[j] = (a, b-1)
                    else:
                        P[j:j+1] = [(a,q-1),(q+1,b)]
                    break
                i += b - a + 1
                j += 1
            P = [(q,q)] + P
        return ans