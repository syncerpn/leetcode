# easy
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def get_surround(r, c):
            k = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    i = r + dr
                    j = c + dc
                    if (i, j) in valids:
                        if board[i][j] == "M":
                            k += 1
            return "B" if k == 0 else str(k)

                    
        i, j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        
        else:
            m, n = len(board), len(board[0])
            valids = set([(i, j) for i in range(m) for j in range(n)])
            s = [(i, j)]
            v = set()
            while s:
                i, j = s.pop()
                if (i, j) in v:
                    continue
                v.add((i, j))
                if board[i][j] != "E":
                    continue
                board[i][j] = get_surround(i, j)
                if board[i][j] == "B":
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di == 0 and dj == 0:
                                continue
                            if (i+di, j+dj) in valids and (i+di, j+dj) not in v:
                                s.append((i+di, j+dj))

        return board