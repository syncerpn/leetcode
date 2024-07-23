# without the head, so we need to swap the values of current node and next node
# then link the node before tail to none
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None