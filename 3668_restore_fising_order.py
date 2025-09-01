# easy
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f = set(friends)
        return [o for o in order if o in f]