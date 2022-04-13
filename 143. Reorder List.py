# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        li = list()
        temp = head
        while temp:
            li.append(temp)
            temp = temp.next
        l = 0
        r = len(li)-1

        while l < r:
            li[l].next = li[r]
            l+=1
            if l == r:
                break
            li[r].next = li[l]
            r-=1
        li[l].next = None
