# easy
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        while v1:
            if v1[-1] != 0:
                break
            v1.pop()
        v2 = list(map(int, version2.split(".")))
        while v2:
            if v2[-1] != 0:
                break
            v2.pop()

        v1, v2 = tuple(v1), tuple(v2)
        return 0 if v1 == v2 else (1 if v1 > v2 else -1)