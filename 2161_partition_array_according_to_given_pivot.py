# O(n) space
# inplace can be done with two-pointer
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        r = []
        m = 0
        for n in nums:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                r.append(n)
            else:
                m += 1
        return l + [pivot] * m + r