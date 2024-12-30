# hacking solution with python permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        for i in itertools.permutations(str(i) for i in range(1, n+1)):
            k -= 1
            if k == 0:
                return "".join(i)
        return ""

# much better with some math involved
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation