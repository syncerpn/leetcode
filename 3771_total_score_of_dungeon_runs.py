# change your perspective
# need revisit
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        st = SortedList()
        res = total = 0
        for d, r in list(zip(damage, requirement))[::-1]:
            st.add(hp + total - r)
            total += d
            res += len(st) - st.bisect_left(total)
        return res