#1. simply travel and compare
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    elif not list2:
        return list1
    
    head = None
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    listm = head

    while list1 and list2:
        if list1.val < list2.val:
            listm.next = list1
            listm = list1
            list1 = list1.next
        else:
            listm.next = list2
            listm = list2
            list2 = list2.next

    if list1:
        listm.next = list1
    elif list2:
        listm.next = list2
    return head
        