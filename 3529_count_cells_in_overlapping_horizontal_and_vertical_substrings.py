# kmp for the search
# line sweep for the count
# set intersection for the result
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        lps = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j and pattern[i] != pattern[j]:
                j = lps[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
        
        def find_occurences(text, pattern):
            result = []
            k = len(pattern)
            j = 0
            for i in range(len(text)):
                while j and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == len(pattern):
                    if result and i - j + 1 <= result[-1][1]:
                        result[-1][1] = i - j + 1 + k
                    else:
                        result.append([i - j + 1, i - j + 1 + k])
                    j = lps[j - 1]
            return result

        m, n = len(grid), len(grid[0])

        htext = "".join(["".join(r) for r in grid])
        vtext = "".join(["".join(c) for c in zip(*grid)])

        hr = find_occurences(htext, pattern)
        vr = find_occurences(vtext, pattern)

        hs = set((i // n, i % n) for l, r in hr for i in range(l, r))
        vs = set((i % m, i // m) for l, r in vr for i in range(l, r))

        return len(hs & vs)