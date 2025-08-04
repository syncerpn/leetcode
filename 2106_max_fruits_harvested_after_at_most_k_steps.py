# sliding window
# trying every possible moving scenario
# generally, we want to move in one direction then turn to the opposite direction
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = startPos + k
        m = len(fruits)
        p = [0] * (n + 2)
        j = 0
        for i in range(n + 1):
            a = 0
            if j < m and fruits[j][0] == i:
                a = fruits[j][1]
                j += 1
            p[i+1] = p[i] + a

        l = max(startPos - k, 0)
        ans = 0
        while l <= startPos:
            d = startPos - l
            r = startPos + max(0, (k - d) // 2, k - 2 * d)
            ans = max(ans, p[r+1] - p[l])
            l += 1
        return ans

# can also optimize run-time with binary search
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def step(R, L):
            return min(startPos - 2 * L + R, 2 * R - startPos - L)
        
        i0 = bisect.bisect_left(fruits, [startPos - k, 0])
        iN = bisect.bisect_right(fruits, [startPos + k + 1, -1])

        ans, wsum, l = 0, 0, i0
        for r in range(i0, iN):
            wsum += fruits[r][1]
            R = fruits[r][0]
            while l <= r and step(R, fruits[l][0]) > k:
                wsum -= fruits[l][1]
                l += 1
            ans=max(ans, wsum)
        return ans