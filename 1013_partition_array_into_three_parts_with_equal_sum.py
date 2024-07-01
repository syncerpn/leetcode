# two pointer trying to reach target sum
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3 != 0:
            return False
        s = s // 3
        i, j = 0, len(arr) - 1
        l, r = arr[i], arr[j]
        while i + 1 < j:
            if l != s:
                i += 1
                l += arr[i]
            elif r != s:
                j -= 1
                r += arr[j]
            else:
                return True

        return False