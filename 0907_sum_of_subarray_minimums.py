# pretty good problem touching monostack + dp/prefix sum
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1000000007

        # we will create a mono increasing stack
        # the stack stores minimums of subarray
        # from the point index i backward to 0
        s = []
        r = 0
        for i in range(len(arr)):
            while s:
                j, tj = s[-1]
                if arr[j] < arr[i]:
                    break
                s.pop()

            (j, tj) = s[-1] if s else (-1, 0)
            # we also store ti which is sum of subarray minimums of arr[:i+1]
            # kinda: ti = sum(arr[k:i+1]) for k in range(i+1)
            ti = tj + arr[i] * (i - j)
            r = (r + ti) % MOD
            s.append((i, ti))

        return r