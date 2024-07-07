# nice problem and beautiful solution using mono stack
# this was my first solution, that uses mono stack to track expandable rectangles
# so for each height, if next height is larger than it, we can "expand" the rectangle width to 2
# i tried to do the expansion and tracking area like that, with forward and backward pass to expand right and left each rectangle
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        n = len(heights)
        area = [0 - h for h in heights] # when doing both forward and backward, be prepared for duplication counting
        for i in range(n):
            c = 0
            while s:
                j = s[-1]
                # if next height is small than a height, we just cannot expand anymore
                # so remove it, and update its expanded area
                if heights[j] <= heights[i]:
                    break
                j = s.pop()
                c += 1
                area[j] += c * heights[j]
            
            if c:
                for j in s:
                    area[j] += c * heights[j]
                
            s.append(i)

        c = 0
        while s:
            j = s.pop()
            c += 1
            area[j] += c * heights[j]
        
        # do one more with backward
        for i in range(n-1,-1,-1):
            c = 0
            while s:
                j = s[-1]
                if heights[j] <= heights[i]:
                    break
                j = s.pop()
                c += 1
                area[j] += c * heights[j]
            
            if c:
                for j in s:
                    area[j] += c * heights[j]
                
            s.append(i)
            
        c = 0
        while s:
            j = s.pop()
            c += 1
            area[j] += c * heights[j]
            
        return max(area)

# but then, it turns out that if we use the same concept
# serveral conditions of left and right expansion are satified without having to track them separately
# so, the optimally clean solution is just sooooo beautiful
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [-1]
        heights.append(0)
        a = 0
        for i in range(len(heights)):
            while heights[i] < heights[s[-1]]:
                hj = heights[s.pop()]
                wj = i - s[-1] - 1
                a = max(a, hj*wj)
            s.append(i)
        return a

# quote an explanation to compliment the math proof
# "This idea is really beautiful.
# However I felt a bit confused when reading the explanation.
# After thinking for a while, here is my thought if it is helpful.
# For any bar x, if it's in a rectangle of which the height is also the height of x, we know that every bar in the rectangle must be no shorter than x.
# Then the issue is to find the left and right boundary where the bars are shorter than x.
# According to the code, when a bar is popped out from the stack, we know it must be higher than the bar at position i,
# so bar[i] must be the right boundary (exclusive) of the rectangle,
# and the previous bar in the stack is the first one that is shorter than the popped one so it must be the left boundary (also exclusive).
# Then we find the rectangle."