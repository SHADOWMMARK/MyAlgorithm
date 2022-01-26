class Solution:
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