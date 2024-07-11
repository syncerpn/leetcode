# two strings should be the same
# or they have exactly two different spots
# track that spots then try swapping
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # assume by default that they have the same length
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
        
        if len(diff_indices) == 0:
            return True
        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return False