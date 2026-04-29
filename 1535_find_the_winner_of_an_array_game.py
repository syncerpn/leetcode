# easy
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        b = arr[0]
        c = 0
        for i in range(1, len(arr)):
            if b > arr[i]:
                c += 1
            else:
                b = arr[i]
                c = 1
            if c == k:
                break
        return b