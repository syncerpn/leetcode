# next_permutation (reimplemented in this solution) + step counting
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num_str = num
        num = list(num)
        n = len(num)
        # kth permutation from num
        for _ in range(k):
            i = n - 2
            while i >= 0:
                if num[i+1] > num[i]:
                    break
                i -= 1
            
            num[i+1:] = num[n-1:i:-1]
            for j in range(i+1, n):
                if num[j] > num[i]:
                    num[i], num[j] = num[j], num[i]
                    break
        
        # simulate adjacent swapping
        m = 0
        for i in range(n):
            if num[i] != num_str[i]:
                j = i + 1
                while num[j] != num_str[i]:
                    j += 1
                while j > i:
                    num[j], num[j-1] = num[j-1], num[j]
                    j -= 1
                    m += 1
        return m