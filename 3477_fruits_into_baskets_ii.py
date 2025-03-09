# pre-idea of segment tree
# of course it is segment tree
# though not very familiar with that yet
# i am happy that at least i have a good feeling
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ss = []
        j = 0
        ans = 0
        for f in fruits:
            i = 0
            while i < len(ss):
                if ss[i][0] >= f:
                    ss[i].popleft()
                    if not ss[i]:
                        ss.pop(i)
                    elif i > 0 and ss[i-1][-1] >= ss[i][0]:
                        ss[i-1] += ss[i]
                        ss.pop(i)
                    break
                i += 1
            else:
                while j < len(baskets):
                    bj = baskets[j]
                    if f <= bj:
                        j += 1
                        break
                    if ss and ss[-1][-1] >= bj:
                        ss[-1].append(bj)
                    else:
                        ss.append(deque([bj]))
                    j += 1
                else:
                    ans += 1
        return ans