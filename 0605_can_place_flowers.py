# just check
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        k = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        i = 1
        while i < k+1:
            if 1 - flowerbed[i-1] and 1 - flowerbed[i] and 1 - flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
                i += 1
                if n == 0:
                    return True
            i += 1        
        return False
