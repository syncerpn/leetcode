# fairly easy
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        D = [abs(a - b) for a, b in zip(nums1, nums2)]
        D.sort(reverse=True)
        n = len(D)
        ans = 0
        for i in range(1, n):
            d = D[i-1] - D[i]
            if d * i <= k:
                k -= d * i
            else:
                s = k // i
                r = k % i
                for j in range(n):
                    if j < r:
                        ans += max(D[i-1] - s - 1, 0) ** 2
                    elif j < i:
                        ans += max(D[i-1] - s, 0) ** 2
                    else:
                        ans += max(D[j], 0) ** 2
                return ans
        else:
            s = k // n
            r = k % n
            for i in range(n):
                if i < r:
                    ans += max(D[-1] - s - 1, 0) ** 2
                else:
                    ans += max(D[-1] - s, 0) ** 2
            return ans
