# easy
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        A = set(list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"))
        B = set(["electronics", "grocery", "pharmacy", "restaurant"])
        ans = {k: [] for k in B}
        for c, b, a in zip(code, businessLine, isActive):
            if a and c and b in B:
                for ci in c:
                    if ci not in A:
                        break
                else:
                    ans[b].append(c)
        return sum([sorted(ans[k]) for k in sorted(ans.keys())], start=[])