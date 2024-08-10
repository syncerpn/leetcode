# three loops for three dots
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(g):
            if g == "0":
                return True
            if g[0] == "0":
                return False
            return 0 <= int(g) <= 255
        
        ans = []
        n = len(s)
        if n < 4:
            return ans
        for i in range(1, n-2):
            if not is_valid(s[0:i]):
                continue
            for j in range(i+1, n-1):
                if not is_valid(s[i:j]):
                    continue
                for k in range(j+1, n):
                    if not is_valid(s[j:k]) or not is_valid(s[k:]):
                        continue
                    ans.append(s[0:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
        return ans