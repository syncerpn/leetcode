# dont hesitate to use extra space for storing the nodes in a hash table/list
# that is probably the way everybody is doing lol
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        r, s = {}, []
        i, h = 0, head
        while h:
            r[h] = i
            new_node = Node(h.val)
            if s:
                s[-1].next = new_node
            s.append(new_node)
            i, h = i + 1, h.next
        
        i, h = 0, head
        while h:
            if h.random:
                s[i].random = s[r[h.random]]
            i, h = i + 1, h.next
        
        return s[0]