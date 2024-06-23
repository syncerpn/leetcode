# keep track of each char's index
# during iteration, if char repeats, update maxlength m if needed and new substring starting location
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        m = 0
        char_dict = {}
        while r < len(s):
            c = s[r]
            if c in char_dict:
                if char_dict[c] >= l:
                    m = r-l if m < r-l else m
                    l = char_dict[c] + 1
            
            char_dict[c] = r
            r += 1

        m = r-l if m < r-l else m
        return m