# text parser
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        A = set(list("abcdefghijklmnopqrstuvwxyz"))
        s = "".join(chunks) + " "
        words = []
        p = []
        for i, c in enumerate(s):
            if c in A:
                p.append(c)
            elif c == "-":
                if p:
                    if p[-1] == "-":
                        while p and p[-1] == "-":
                            p.pop()
                        words.append("".join(p))
                        p = []
                    else:
                        p.append(c)
            else:
                if p:
                    while p and p[-1] == "-":
                        p.pop()
                    words.append("".join(p))
                    p = []
        d = Counter(words)
        return [d[q] for q in queries]
