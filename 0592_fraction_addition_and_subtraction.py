# text parse and gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        i, m = 0, 1
        if expression[0] == "-":
            i, m = 1, -1
        
        x, y = 0, 0
        a, b = 1, 0

        to_de = False
        expression += "+"
        while i < len(expression):
            c = expression[i]
            if c == "+" or c == "-":
                y *= m
                if b == 0:
                    b = 1

                z = gcd(a, b)
                x = x * b // z + y * a // z
                a = a // z * b
                z = gcd(x, a)
                x //= z
                a //= z

                y, b = 0, 0
                m = 1 if c == "+" else -1
                to_de = False
            elif c == "/":
                to_de = True
            elif to_de:
                b = b * 10 + int(c)
            else:
                y = y * 10 + int(c)
            i += 1

        return str(x) + "/" + str(a)