# simple stack
class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        n = len(types)
        s = []
        for i in range(n):
            if not s or types[i] != s[-1][0] or colors[i] != s[-1][1]:
                if groupSize[types[i]] > 1:
                    s.append([types[i], colors[i], 1])
            else:
                s[-1][2] += 1
                if s[-1][2] == groupSize[s[-1][0]]:
                    s.pop()
        return not s
