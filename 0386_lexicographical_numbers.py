# append 0 at the end until we cant
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        for _ in range(n-1):
            a = ans[-1] * 10
            while a > n:
                a //= 10
                a += 1
                while a % 10 == 0:
                    a //= 10
            ans.append(a)
        return ans