# for practicing backtracking
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        def backtrack(s, indices):
            for i in indices:
                r = s + tiles[i]
                result.add(r)
                backtrack(r, [j for j in indices if j != i])
        
        backtrack("", list(range(len(tiles))))
        return len(result)

# computational solution
# n! / (m[1]! * m[2]! * .. * m[i]!)
# where m[i] is count of a character
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        record = [0] * 26
        for tile in tiles: record[ord(tile)-ord('A')] += 1
        def dfs(record):
            s = 0
            for i in range(26):
                if not record[i]: continue
                record[i] -= 1
                s += dfs(record) + 1 
                record[i] += 1
            return s    
        return dfs(record)