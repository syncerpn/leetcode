# greedy builder
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        _a = ord("a")
        _z = ord("z")

        n = len(s)
        d = Counter(list(s))
        ans = []
        def helper(i):
            if i == n:
                return False
            c = target[i]
            if d[c] > 0:
                ans.append(c)
                d[c] -= 1
                if helper(i + 1):
                    return True
                ans.pop()
                d[c] += 1

            _c = ord(c)
            for _cc in range(_c+1, _z+1):
                cc = chr(_cc)
                if d[cc] > 0:
                    ans.append(cc)
                    d[cc] -= 1
                    return True
            return False
        
        helper(0)
        for _c in range(_a, _z+1):
            c = chr(_c)
            ans += [c] * d[c]
        ans = "".join(ans)
        return ans if ans > target else ""