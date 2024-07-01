# simulate writing and count it
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alpb = "abcdefghijklmnopqrstuvwxyz"
        d = {a: w for a, w in zip(alpb, widths)}
        n_lines = 1
        line = 0
        for c in s:
            if line + d[c] > 100:
                n_lines += 1
                line = 0
            line += d[c]
        
        return [n_lines, line]