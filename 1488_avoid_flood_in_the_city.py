# harder than it looks at first
# because you cannot make an empty lake "more empty"
# sortedlist is needed
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
        return ans

# this one has lower actual runtime
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        h   = {}
        q   = deque([])
        res = []
        for i, x in enumerate(rains):
            if x:
                if x in h:
                    for j in q:
                        if j > h[x]:
                            res[j] = x
                            q.remove(j)
                            break
                    else:
                        return []
                res.append(-1)
                h[x] = i
            else:
                res.append(1)
                q.append(i)
        return res