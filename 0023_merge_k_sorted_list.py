#1. we will keep checking for the smallest node
#2. keep them sorted and saved into a reference list
#3. smallest node will be assign to the next node in the merged list and go next
#4. make sure after going next, the reference list is still sorted, simply by bubbling
#5. if going next resulting in None, we increase the reference index of the smallest node, r
#6. repeat until only one ListNode remains
#7. merge it with the merged list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(lists: list) -> ListNode:
    lists = [l for l in lists if l]
    if len(lists) == 1:
        return lists[0]
    if len(lists) == 0:
        return None

    lists = sorted(lists, key=lambda x: x.val)
    head = None
    listm = None
    r = 0
    n = len(lists)

    while r < n-1:
        if not head:
            head = lists[r]
            listm = head
        else:
            listm.next = lists[r]
            listm = lists[r]
        
        lists[r] = lists[r].next
        if lists[r] is None:
            r += 1
        else:
            i = r
            while i < n-1:
                if lists[i].val < lists[i+1].val:
                    break
                tmp = lists[i]
                lists[i] = lists[i+1]
                lists[i+1] = tmp
                i += 1
        
    listm.next = lists[r]
    return head