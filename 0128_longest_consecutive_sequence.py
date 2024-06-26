# interesting problem, because you must write algorithm that runs in O(n)
# im happy i solved it, with set
# this solution is likely truely two-pass
# one to build the num set
# another iterate the set and check a number's left and right consecutive partner
# remove items that has done checking so that you dont check them again anymore
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l_max = 0
        while s:
            c_max = s.pop()
            c_min = c_max
            
            # try expanding right
            while c_max+1 in s:
                s.remove(c_max+1)
                c_max += 1

            # try expanding left
            while c_min-1 in s:
                s.remove(c_min-1)
                c_min -= 1
            
            # then we can build the sequence from c_min to c_max inclusively
            l = c_max - c_min + 1
            l_max = max(l, l_max)
        
        return l_max