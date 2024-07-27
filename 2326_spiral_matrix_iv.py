# going spiral
# make a turn if need
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def turn(h, v):
            if h == 1: h, v = 0, 1
            elif v == 1: h, v = -1, 0
            elif h == -1: h, v = 0, -1
            else: h, v = 1, 0
            return h, v

        i, j = 0, 0
        h, v = 1, 0
        v = 0
        ans = [[-1] * n for _ in range(m)]
        while head:
            ans[i][j] = head.val
            head = head.next
            if i + v >= m or i + v < 0 or j + h >= n or j + h < 0 or ans[i+v][j+h] != -1:
                h, v = turn(h, v)
            i, j = i + v, j + h
        
        return ans