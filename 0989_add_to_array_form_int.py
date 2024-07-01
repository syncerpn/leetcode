# not so clean, but inplace saves a lot of time
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1
        c = 0
        while i >= 0 or k > 0:
            d = k % 10
            k //= 10
            n = 0
            if i >= 0:
                n = num[i]
            s = n + d + c
            c = 0
            if s >= 10:
                c = 1
                s = s - 10
            if i >= 0:
                num[i] = s
                i -= 1
            else:
                num.insert(0, s)
        if c:
            num.insert(0, 1)
        return num