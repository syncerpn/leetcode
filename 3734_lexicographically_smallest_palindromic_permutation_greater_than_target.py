# build one half with a center
# then check the requirement
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        d = Counter(s)
        
        def check():
            return all(v >= 0 for v in d.values())

        center = ""
        for c in d:
            v = d[c]
            if v % 2 == 0:
                continue
            if center:
                return ""
            center = c
            d[c] -= 1

        n = len(s)
        half = n // 2
        for i, w in enumerate(target[:half]):
            d[w] -= 2

        if check():
            head = target[:half]
            tail = center + head[::-1]
            if tail > target[half:]:
                return head + tail

        for i in range(half - 1, -1, -1):
            w = target[i]
            d[w] += 2
            if not check(): continue

            for j in range(ord(w) - ord("a") + 1, 26):
                x = ascii_lowercase[j]
                if d[x] == 0: continue

                d[x] -= 2
                result = list(target[:i + 1])
                result[i] = x

                for x in ascii_lowercase:
                    result.extend(x * (d[x] // 2))

                tail = result[::-1]
                result.append(center)
                result += tail

                return "".join(result)

        return ""
        