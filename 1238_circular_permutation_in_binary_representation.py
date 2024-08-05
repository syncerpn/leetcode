# works but slow
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        d = [0,1,1,0]
        b = [0] * n
        ans = [0]
        k = 0
        for i in range((1 << n) - 1):
            j = 0
            b[j] += 1
            while b[j] == 2 or b[j] == 4:
                if b[j] == 4:
                    b[j] = 0
                j += 1
                b[j] += 1
            m = sum(d[b[j]] << j for j in range(n))
            if m == start:
                k = i+1
            ans.append(m)
        return ans[k:] + ans[:k]

# gray code is crazily beautiful
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ i >> 1 for i in range(1 << n)]