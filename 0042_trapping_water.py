#1. we use two pointer to keep track of the highest wall from l and r that creates trap of water
#2. if a wall inbetween is shorter than left and right walls, water is trapped
#3. else if a wall is higher than left (or right), it creates a higher trap with the right (or left)
def solve(height: int) -> int:
    li = 0
    ri = len(height) - 1

    max_l = height[li]
    max_r = height[ri]

    w = 0

    while li < ri:
        if max_l < max_r:
            li += 1
            if max_l < height[li]:
                max_l = height[li]
            else:
                w += max_l - height[li]
        else:
            ri -= 1
            if max_r < height[ri]:
                max_r = height[ri]
            else:
                w += max_r - height[ri]
    
    return w