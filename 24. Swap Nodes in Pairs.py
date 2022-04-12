# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

#recursive solution:
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not ( head and head.next ): return head
        nex = ListNode
        nex = head.next
        head.next = self.swapPairs(nex.next)
        nex.next = head
        return nex

#non-recursive solution: (need to create a "fake" head node in order to return)
     def swapPairs(self, head: ListNode) -> ListNode:
        if not ( head and head.next ): return head
        pre = ListNode
        pre.next = head
        temp = ListNode
        temp = pre
        while temp.next and temp.next.next:
            l = ListNode
            r = ListNode 
            l = temp.next
            r = temp.next.next
            temp.next = r
            l.next = r.next
            r.next = l
            temp = l
        return pre.next
      
#(interesting that the recursive solution is slower then the non-recursive one)
