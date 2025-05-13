# lee's solution
# the problem is easy, but implementation to not get tle is not
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(A):
            seen = set()
            top = 0
            for i, r in enumerate(A):
                seen |= set(r)
                top += sum(r)
                bot = total - top
                if top - bot in [0, A[0][0],  A[0][-1], A[i][0]]: return True
                if len(A[0]) > 1 and i > 0 and top - bot in seen: return True
            return False
        
        total = sum(sum(r) for r in grid)
        if check(grid) or check(grid[::-1]): return True
        grid = list(zip(*grid))
        return check(grid) or check(grid[::-1])

# still lee's solution, but i modified a bit
# the first condition is kind of bugging me out
# because one of the rect corners is missing from the check
# shouldnt it be: "if top - bot in [0, A[0][0],  A[0][-1], A[i][0], A[i][-1]]: return True"
# but the better is, you can remove A[0][-1]
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(A):
            seen = set()
            top = 0
            for i, r in enumerate(A):
                seen |= set(r)
                top += sum(r)
                bot = total - top
                if top - bot in [0, A[0][0], A[i][0]]: return True
                if len(A[0]) > 1 and i > 0 and top - bot in seen: return True
            return False
        
        total = sum(sum(r) for r in grid)
        if check(grid) or check(grid[::-1]): return True
        grid = list(zip(*grid))
        return check(grid) or check(grid[::-1])