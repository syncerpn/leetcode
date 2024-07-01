# simulate rock move
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rhi = 0
        rwi = 0
        for i in range(64):
            wi = i % 8
            hi = i // 8
            if board[hi][wi] == "R":
                rhi = hi
                rwi = wi
                break
        
        c = 0
        for d in [(0,1), (0,-1), (1,0), (-1,0)]:
            dh, dw = d
            hi = rhi + dh
            wi = rwi + dw
            while 0 <= hi < 8 and 0 <= wi < 8:
                if board[hi][wi] == "B":
                    break
                elif board[hi][wi] == "p":
                    c += 1
                    break
                hi += dh
                wi += dw
        return c

# or string manip
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rhi = 0
        rwi = 0
        for i in range(64):
            wi = i % 8
            hi = i // 8
            if board[hi][wi] == "R":
                rhi = hi
                rwi = wi
                break
        w = ""
        for i in board[rhi]:
            if i != ".":
                w += i
        h = ""
        for hi in range(8):
            if board[hi][rwi] != ".":
                h += board[hi][rwi]
        return ("pR" in w) + ("Rp" in w) + ("pR" in h) + ("Rp" in h)
