# fairly simple
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = [False] * len(rooms)
        v[0] = True
        s = set(rooms[0])
        while s:
            i = s.pop()
            v[i] = True
            for j in rooms[i]:
                if not v[j]:
                    s.add(j)
        return all(v)