# backtracking
# deal with the floating result
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = "+-*/"

        def f(a, b, x):
            if   x == "+": return a + b
            elif x == "-": return a - b
            elif x == "*": return a * b
            elif x == "/": return 0 if b == 0 else a / b

        def get_op_seq(k):
            x, y, z = k % 4, (k // 4) % 4, k // 16
            return ops[x], ops[y], ops[z]

        e = float(inf)
        for cc in itertools.permutations(cards):
            a, b, c, d = cc
            for k in range(64):
                x, y, z = get_op_seq(k)
                e = min(e,
                    abs(f(a, f(b, f(c, d, z), y), x) - 24),
                    abs(f(a, f(f(b, c, y), d, z), x) - 24),
                    abs(f(f(a, b, x), f(c, d, z), y) - 24),
                    abs(f(f(f(a, b, x), c, y), d, z) - 24),
                    abs(f(f(a, f(b, c, y), x), d, z) - 24),
                )
                if e <= 10e-6:
                    return True
        return False

# short and concise version, lol
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return math.isclose(cards[0], 24)
        return any(self.judgePoint24([x] + rest)
                for a, b, *rest in itertools.permutations(cards)
                for x in {a+b, a-b, a*b, b and a/b})