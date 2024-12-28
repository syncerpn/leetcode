# my dp solution which is not memory-efficient
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        q = []
        s = 0
        for i, a in enumerate(nums):
            if i >= k:
                q.append(s)
                s -= nums[i-k]
            s += a
        q.append(s)
        m = q[0] + q[k] + q[2*k]
        dp0 = [(q[0], 0)]
        dp1 = []
        dp2 = []
        for i, a in enumerate(q):
            if i == 0:
                continue
            n, j = dp0[i-1]
            dp0.append((n, j) if n >= a else (a, i))
            if i >= k:
                if i == k:
                    n, j = dp0[i-k]
                    dp1.append((n+a, j, i))
                else:
                    n, j = dp0[i-k]
                    p, k0, k1 = dp1[i-k-1]
                    dp1.append((n+a, j, i) if n+a > p else (p, k0, k1))
            if i >= 2 * k:
                if i == 2 * k:
                    n, j0, j1 = dp1[i-2*k]
                    dp2.append((n+a, j0, j1, i))
                else:
                    # print(dp1[i-k])
                    n, j0, j1 = dp1[i-2*k]
                    p, k0, k1, k2 = dp2[i-2*k-1]
                    dp2.append((n+a, j0, j1, i) if n+a > p else (p, k0, k1, k2))
        _, *ans = dp2[-1]
        return ans

# this actually can be solved with O(n) time O(1) space using three pointers and sliding window
# how crazy
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k*2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq