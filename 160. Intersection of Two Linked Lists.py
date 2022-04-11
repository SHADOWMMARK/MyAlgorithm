# Given the heads of two singly linked-lists headA and headB, 
# return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## first idea is normal and easy but also doing well, is using diction(hashtable)to store all nodes of one linkedlist

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        while headA:
            d[headA] = headA.val
            headA = headA.next
        while headB:
            if headB in d:
                return headB
            else:
                headB = headB.next
        return 

      
 ## second way of solution is kind of tricky: 
 ## let us see the code first
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
      
## notice that we use two pointers to denote the location, we can guess two linkedlist as a linkedlist has len(m) and b linkedlist has len(n)
   # if they got public part then m = a + c; n = b + c
   # then we can divide two situations: if they have common part: 1.a=b then they will return the overlap node after they move a=b steps;
   #  2. a!=b but we notice a + c + b = b + c + a, which is saying that after the pointer A (B) reach the end of a (b) then we put it at the head of b (a) 
   # then they will also meet at the first overlapped node.
    # the second situation is that if they do not overlap then A != B always holds.

    
# problem No.142 is also similar with this, it can also use the hashtable to get rid easily, and  can also use low and fast pointer to get rid of problems.
