# brute force solution
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 0
        while memory1 >= 0 and memory2 >= 0:
            i += 1
            if memory1 >= memory2:
                if memory1 < i:
                    break
                memory1 -= i
            else:
                if memory2 < i:
                    break
                memory2 -= i
        return [i, memory1, memory2]

# O(1) solution is quite complicated