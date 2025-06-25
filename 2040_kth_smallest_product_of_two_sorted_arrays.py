# need to handle pos and neg numbers
# lee's solution, need revisit
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        neg1, pos1 = [-a for a in nums1 if a < 0][::-1], [a for a in nums1 if a >= 0]
        neg2, pos2 = [-a for a in nums2 if a < 0][::-1], [a for a in nums2 if a >= 0]

        neg = len(neg1) * len(pos2) + len(neg2) * len(pos1)
        if k > neg:
            k -= neg
            s = 1
        else:
            k = neg - k + 1
            neg2, pos2 = pos2, neg2
            s = -1

        def count(A, B, x):
            res = 0
            j = len(B) - 1
            for i in range(len(A)):
                while j >= 0 and A[i] * B[j] > x:
                    j -= 1
                res += j + 1
            return res

        left, right = 0, 10**10
        while left < right:
            mid = (left + right) // 2
            if count(neg1, neg2, mid) + count(pos1, pos2, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left * s
        