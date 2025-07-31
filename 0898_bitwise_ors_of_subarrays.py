# dp and hash
# the solution is not that difficult to think of
# but i was too concerned about the complexity which looks like O(n2)
# but actually provable to be only O(32n)
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s = set()
        v = set()
        for a in arr:
            s_next = set()
            for b in s:
                s_next.add(b | a)
                v.add(b | a)
            s_next.add(a)
            v.add(a)
            s = s_next
        
        return len(v)

# shorter
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s, v = set(), set()
        for a in arr:
            s = set(b | a for b in s)
            s.add(a)
            v |= s
        
        return len(v)