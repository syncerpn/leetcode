# nice problem usually has short name lol
# happy that i solved it myself with O(1) space
# trivial solution would be generating array of candies to simulate the distribution
# however, we can calculate them on the fly
# the below code may not be clean, but might be good to help others understand the algorithm
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # we will check the rating slope, i.e. whether the rating keeps going up or down
        # by tracking l and h which are indices of low and high position
        # if l < h, the slope is going up
        # if l > h, the slope is going down
        h, l = 0, 0
        s = 0 # the total amount of candies
        i = 0
        p = 0 # height of the tail (the last point) of the previous slope
        for a, b in pairwise(ratings):
            if b < a:
                if h > l:
                    # this is the turning point of a going-up slope to going-down
                    # at this point, we will calculate the number of candies distributed to all others within the range [l, r]
                    # the tail is a common points between two slopes, so we need to remove the duplicated count of p
                    s += (h - l + 1) * (h - l + 2) // 2 - p
                    p = h - l + 1 # for going-up slope, height of tail is h - l + 1, assuming optimal distribution
                    l = i # prepare for the next slope
                l += 1
            elif b > a:
                if h < l:
                    s += (l - h + 1) * (l - h + 2) // 2 - min(p, l - h + 1)
                    p = 1 # for going-down slope, height of tail is 1, assuming optimal distribution
                    h = i # prepare for the next slope
                h += 1
            else:
                # if two points have the height (same rating), conclude the last slope
                s += (abs(h - l) + 1) * (abs(h - l) + 2) // 2 - min(p, abs(h - l) + 1)
                p = 0
                h = l = i + 1
                
            i += 1
        
        # conclude the final slop
        s += (abs(h - l) + 1) * (abs(h - l) + 2) // 2 - min(p, abs(h - l) + 1)
        return s

# same idea but compact and clean
# now we distribute candies on the way
class Solution:
    def candy(self, ratings: List[int]) -> int:
        h, l, p = 0, 0, 0
        s = 1
        
        for a, b in pairwise(ratings):
            if a < b:
                h, l, p = h + 1, 0, h + 1
                s += 1 + h
            elif a == b:
                h = l = p = 0
                s += 1
            else:
                h, l = 0, l + 1
                s += 1 + l - int(p >= l)
        
        return s

# also this is brute force/simulation solution
# copied from others
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n 

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)