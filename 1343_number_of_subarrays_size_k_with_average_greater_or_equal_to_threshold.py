# easy with sliding window + prefix sum
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        p = 0
        threshold = threshold * k
        ans = 0

        for i in range(len(arr)):
            p += arr[i]
            if i >= k:
                p -= arr[i-k]
            if i >= k - 1:
                if p >= threshold:
                    ans += 1

        return ans