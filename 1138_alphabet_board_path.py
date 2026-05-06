# special z case lol
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = {c: (i, j) for i, g in enumerate(board) for j, c in enumerate(g)}
        a = "a"
        ans = ""
        for b in target:
            ay, ax = d[a]
            by, bx = d[b]
            dy = by - ay
            dx = bx - ax
            if a == "z":
                ans += abs(dy) * ("D" if dy > 0 else "U")
                ans += abs(dx) * ("R" if dx > 0 else "L")
            else:
                ans += abs(dx) * ("R" if dx > 0 else "L")
                ans += abs(dy) * ("D" if dy > 0 else "U")
            ans += "!"
            a = b
        return ans