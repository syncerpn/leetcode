# binary search is fine
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        l = 1
        r = int(((red + blue) * 2) ** 0.5)
        a, b = 0, 0
        while l <= r:
            m = (l + r) // 2
            if m % 2:
                a = (1 + m) * ((m - 1) // 2 + 1) // 2
                b = (2 + m - 1) * ((m - 3) // 2 + 1) // 2
            else:
                a = m * ((m - 2) // 2 + 1) // 2
                b = (2 + m) * ((m - 2) // 2 + 1) // 2
            if (a <= blue and b <= red) or (a <= red and b <= blue):
                l = m + 1
            else:
                r = m - 1
        
        return l - 1

# but math is still more beautiful
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red > blue:
            red, blue = blue, red

        # number of odd rows
        odd = isqrt(red)
        # sum of even rows when number of odd rows == number of even rows
        even_sum = odd ** 2 + odd
        
        # even rows are red, odd rows are blue
        if even_sum <= red and even_sum + odd + 1 <= blue:
            return odd * 2 + 1
        
        # odd rows are red, even rows are blue
        if even_sum <= blue:
            return odd * 2
        
        # odd rows are red but there is 1 less odd row, even rows are blue
        return odd * 2 - 1