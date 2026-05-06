# simulation is naive
# this observation is the real deal
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        w = z = 0
        j = s.rfind('1')
    
        for i in range(j + 1):
			# increase waiting time if we come across 2 conseq 1's
			# however, if there are no zeroes to the left, then there is no waiting time
            if i > 0 and s[i] == '1' and s[i - 1] == '1' and z > 0:
                w += 1
            
			# decrease waiting time if we come across 2 conseq 0's
            if i > 0 and s[i] == '0' and s[i - 1] == '0' and w > 0:
                w -= 1
            
            if s[i] == '0':
                z += 1
                
        return z + w