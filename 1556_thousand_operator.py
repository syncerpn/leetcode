# its simple
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)
            
        s = f"{n % 1000:03}"
        n = n // 1000
        while n >= 1000:
            s = f"{n % 1000:03}" + "." + s
            n //= 1000
        
        return f"{n}" + "." + s if n > 0 else s