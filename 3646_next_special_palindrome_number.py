# the problem is not difficult
# feel bad not complete the implementation during the contest
# we pre-build some milestone based on input length
# then bruteforce all valid palindromes that has the same length as the input
class Solution:
    def specialPalindrome(self, n: int) -> int:
        milestones = [1, 22, 212, 4444, 23332, 244442, 2441442, 26666662, 234434432, 2888888882, 23666366632,
                    244666666442, 2388883888832, 24488888888442, 234466636664432, 2666888888886662, 23448888388884432]

        m = len(str(n))
        ans = [milestones[m]]
        
        q = []
        def distribute(m, p, qi):
            if m == 0:
                if sum(j % 2 for j in qi) < 2:
                    q.append([j for j in qi])
            else:
                for i in range(p, min(10, m+1)):
                    distribute(m-i, i+1, qi+[i])
        distribute(m, 1, [])

        s = [0] * m
        def gen_num(d, i):
            if i >= m - m // 2:
                ss = sum(a * (10 ** i) for i, a in enumerate(s))
                if ss > n:
                    ans[0] = min(ans[0], ss)
            else:
                kk = sorted(list(d.keys()))
                for k in kk:
                    if i < len(s) // 2:
                        if d[k] > 1:
                            d[k] -= 2
                            s[i] = k
                            s[~i] = k
                            gen_num(d, i+1)
                            d[k] += 2
                    elif len(s) % 2 and i == len(s) // 2 and d[k] == 1:
                        d[k] -= 1
                        s[i] = k
                        gen_num(d, i+1)
                        d[k] += 1
        for qi in q:
            gen_num({a: a for a in qi}, 0)
        return ans[0]