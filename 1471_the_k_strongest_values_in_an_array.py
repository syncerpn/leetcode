# sorting
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        arr.sort(key=lambda a: (abs(a-m), a), reverse=True)
        return arr[:k]