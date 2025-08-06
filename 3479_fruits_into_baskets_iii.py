# good intro to segment tree
# very nice solution
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        class SegmentTree:
            def __init__(self, A):
                self.n = 2 ** math.ceil(math.log2(len(A)))
                self.A = [0] * (2 * self.n)
                for i, a in enumerate(A):
                    self.update(i + self.n, a)
            
            def update(self, i, a):
                self.A[i] = a
                while i > 1:
                    i = i >> 1
                    self.A[i] = max(self.A[i*2], self.A[i*2+1])
            
            def find(self, v):
                if self.A[1] < v:
                    return -1
                i = 1
                while i < self.n:
                    if self.A[i*2] >= v:
                        i = i * 2
                    else:
                        i = i * 2 + 1
                return i
        
        st = SegmentTree(baskets)
        ans = 0
        for f in fruits:
            i = st.find(f)
            if i != -1:
                st.update(i, -1)
            else:
                ans += 1
        return ans