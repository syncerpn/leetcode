# backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def backtrack(k, p, v):
            x, y = p
            c = word[k]
            if board[x][y] != c:
                return False
            
            if k == len(word) - 1:
                return True
            
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for q in neighbors:
                if q in v:
                    i, j = q
                    v.discard(q)
                    if backtrack(k+1, q, v):
                        return True
                    v.add(q)
            return False
        
        v = set((i, j) for i in range(m) for j in range(n))
        for i in range(m):
            for j in range(n):
                v.discard((i, j))
                if backtrack(0, (i, j), v):
                    return True
                v.add((i, j))

        return False