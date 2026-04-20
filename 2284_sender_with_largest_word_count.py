# easy
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = {}
        for s, m in zip(senders, messages):
            if s not in d:
                d[s] = 0
            d[s] += len(m.split(" "))
        
        ans, mm = "", 0
        for s in d:
            m = d[s]
            if m > mm:
                ans = s
                mm = m
            elif m == mm and ans < s:
                ans = s
        
        return ans