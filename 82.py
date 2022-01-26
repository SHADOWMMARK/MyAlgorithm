# when considering about the situation dealing with the tree or listnodes there always a recursion solution.
# This problem is asking us to delete the duplicated listnodes
# recursion solution:


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    if head.val!=head.next.val:
        head.next = self.deleteDuplicates(head.next)
    else:
        temp = head.next
        while temp and head.val==temp.val:
            temp = temp.next
        return self.deleteDuplicates(temp)
    return head
    
#none-recursion solution:
#prepare a dummy first node in case the first node in the nodelist be deleted:

def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    cur, r =ListNode(0), head
    cur.next = head
    l = cur
    while r:
        while r.next and r.val==r.next.val:
            r=r.next
        if l.next==r:
            l = l.next
        else:
            l.next = r.next
        r = r.next
    return cur.next
    
