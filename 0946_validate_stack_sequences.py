# simulate it
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for p in popped:
            while not s or s[-1] != p:
                if i >= len(pushed):
                    return False
                s.append(pushed[i])
                i += 1
            if not s:
                return False
            s.pop()
        return True

# even more beautiful with O(1) space solution
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i - 1, j + 1
            i += 1
        return i == 0