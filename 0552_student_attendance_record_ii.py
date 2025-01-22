# dp obviously, and also named DFA, NFA, state machine
# this natural memoi somehow passed all the cases but still raised memory exceeded lol
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        @functools.cache
        def extend(a, l, n):
            if n == 0:
                return 1
            if n == 1:
                return 3 - a - (l == 2)
            k = n - 2
            if not a and l == 0:
                r = 2*extend(False,0,k) + 1*extend(False,1,k) + 1*extend(False,2,k) + 3*extend(True,0,k) + 1*extend(True,1,k)
            elif not a and l == 1:
                r = 2*extend(False,0,k) + 1*extend(False,1,k) + 3*extend(True,0,k) + 1*extend(True,1,k)
            elif not a and l == 2:
                r = 1*extend(False,0,k) + 1*extend(False,1,k) + 2*extend(True,0,k) + 1*extend(True,1,k)
            elif l == 0:
                r = 2*extend(True,0,k) + 1*extend(True,1,k) + 1*extend(True,2,k)
            elif l == 1:
                r = 2*extend(True,0,k) + 1*extend(True,1,k)
            elif l == 2:
                r = 1*extend(True,0,k) + 1*extend(True,1,k)
            return r % MOD
        return extend(False,0,n)

# but ofcourse we can compress the space
# MOD in between is necessary to avoid big num computation
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp00, dp01, dp02, dp10, dp11, dp12 = 1, 1, 0, 1, 0, 0
        for _ in range(1, n):
            dp00, dp01, dp02, dp10, dp11, dp12 = (dp00 + dp01 + dp02) % MOD, dp00, dp01, (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % MOD, dp10, dp11
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % MOD

# log(n) solution with matrix mul
# pretty hard to understand
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        import numpy as np
        def matrixPow(matrix: np.ndarray, n: int, mod: int) -> np.ndarray:
            if n == 1:
                return matrix
            matrix_squared = np.mod(matrix @ matrix, mod)
            if (n % 2) == 0:
                return matrixPow(matrix_squared, n // 2, mod)
            return np.mod(matrix @ matrixPow(matrix_squared, (n - 1) // 2, mod), mod)
        
        state = np.array([1, 0, 0, 0, 0, 0], dtype=np.uint64)
        trans = np.array([
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
        ], dtype=np.uint64)

        trans_pow = matrixPow(trans, n, MOD)
        return int(np.sum(trans_pow[:, 0]) % MOD)

# following is quite similar to the above, yet much much faster
# should be studied why
import numpy as np


class Solution:

    MOD = 10 ** 9 + 7

    def checkRecord(self, n: int) -> int:
        state = np.array([1, 0, 0, 0, 0, 0], dtype=np.uint64)
        trans = np.array([
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
        ], dtype=np.uint64)

        trans_pow = self.matrixPow(trans, n, self.MOD)
        return int(np.sum(trans_pow[:, 0]) % self.MOD)

    def matrixPow(self, matrix: np.ndarray, n: int, mod: int) -> np.ndarray:
        if n == 1:
            return matrix
        matrix_squared = np.mod(matrix @ matrix, mod)
        if (n % 2) == 0:
            return self.matrixPow(matrix_squared, n // 2, mod)
        return np.mod(matrix @ self.matrixPow(matrix_squared, (n - 1) // 2, mod), mod)