# tagged as medium
# looked easy at first
# solved like a hard one
# really need to consider lots of cases
class Solution:
    def makeParityAlternating(self, nums: List[int]) -> List[int]:
        o, o_mi, o_ma, o_ni, o_na = 0, inf, -inf, inf, -inf
        e, e_mi, e_ma, e_ni, e_na = 0, inf, -inf, inf, -inf
        for i, a in enumerate(nums):
            if a % 2 != i % 2:
                e += 1
                e_ni = min(e_ni, a)
                e_na = max(e_na, a)
            else:
                e_mi = min(e_mi, a)
                e_ma = max(e_ma, a)
            
            if a % 2 == i % 2:
                o += 1
                o_ni = min(o_ni, a)
                o_na = max(o_na, a)
            else:
                o_mi = min(o_mi, a)
                o_ma = max(o_ma, a)

        if o_na != o_ni:
            o_ans = max(o_ma, o_na-1) - min(o_mi, o_ni+1)
        else:
            o_ans = min(max(o_ma, o_na-1) - min(o_mi, o_ni-1), max(o_ma, o_na+1) - min(o_mi, o_ni+1))
        if e_na != e_ni:
            e_ans = max(e_ma, e_na-1) - min(e_mi, e_ni+1)
        else:
            e_ans = min(max(e_ma, e_na-1) - min(e_mi, e_ni-1), max(e_ma, e_na+1) - min(e_mi, e_ni+1))
        if o < e:
            return o, o_ans
        if e < o:
            return e, e_ans
        return o, min(o_ans, e_ans)