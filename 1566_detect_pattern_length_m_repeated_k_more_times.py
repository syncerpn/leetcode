# no need to overcomplicate this problem
# we just need to compare elements of each pattern (index shifted by m)
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        c = 0
        for i in range(len(arr)-m):
            if arr[i] != arr[i+m]:
                c = 0
            else:
                c += 1
                if c >= (k-1) * m:
                    return True
        return False