# O(n2) probably works, but this is O(n)
# with two pointers moving in the opposite directions, keep updating smaller height of the pair
# math proof is available online
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        m = (j-i) * min(height[i], height[j])
        while i != j-1:
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            t = (j-i) * min(height[i], height[j])
            m = t if m < t else m
        
        return m