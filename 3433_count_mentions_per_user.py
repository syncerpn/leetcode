# need to read the description more carefully
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        h = deque()
        onl = [True] * numberOfUsers
        ans = [0] * numberOfUsers
        events.sort(key=lambda e: (int(e[1]), e[0][2]))
        for m, t, s in events:
            t = int(t)
            while h and h[0][0] <= t:
                _, i = h.popleft()
                onl[i] = True
            if m == "MESSAGE":
                if s == "ALL":
                    for i in range(numberOfUsers):
                        ans[i] += 1
                elif s == "HERE":
                    for i in range(numberOfUsers):
                        if onl[i]:
                            ans[i] += 1
                else:
                    for c in s.split(" "):
                        i = int(c[2:])
                        ans[i] += 1

            elif m == "OFFLINE":
                i = int(s)
                onl[i] = False
                h.append((t + 60, i))
        
        return ans