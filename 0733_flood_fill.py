# bfs should work
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ref_color = image[sr][sc]
        if color == ref_color:
            return image

        h = len(image)
        w = len(image[0])
        
        visited = [[False for _ in range(w)] for _ in range(h)]
        visited[sr][sc] = True

        s = [(sr, sc)]
        while s:
            r, c = s.pop()
            if image[r][c] != ref_color:
                continue
            image[r][c] = color

            if r - 1 >= 0:
                if not visited[r-1][c]:
                    s.append((r-1, c))
                    visited[r-1][c] = True
            if r + 1 < h:
                if not visited[r+1][c]:
                    s.append((r+1, c))
                    visited[r+1][c] = True
            if c - 1 >= 0:
                if not visited[r][c-1]:
                    s.append((r, c-1))
                    visited[r][c-1] = True
            if c + 1 < w:
                if not visited[r][c+1]:
                    s.append((r, c+1))
                    visited[r][c+1] = True
        return image