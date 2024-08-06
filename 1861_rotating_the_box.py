# feel like advent of code, lol
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            c = 0
            for j in range(n+1):
                if j == n or box[i][j] == "*":
                    for k in range(j-c, j):
                        box[i][k] = "#"
                    c = 0
                else:
                    if box[i][j] == "#":
                        c += 1
                    box[i][j] = "."

        return zip(*box[::-1])