#first way is to make a new linkedList
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        begin = ListNode(0)
        curr = begin
        k = 0
        while l1 or l2 or k != 0:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            s = l1v+l2v+k
            k = s//10
            temp = ListNode(s%10)
            curr.next = temp
            curr = temp
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return begin.next
