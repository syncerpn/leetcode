# un-xor is easy
# inplace solution with python is just beautiful
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        p = pref[0]
        for i in range(1, len(pref)):
            p, pref[i] = pref[i], pref[i] ^ p
        return pref