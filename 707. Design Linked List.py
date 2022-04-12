# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
# Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

  # MyLinkedList() Initializes the MyLinkedList object.
  # int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.

  # void addAtHead(int val) Add a node of value val before the first element of the linked list. 
  # After the insertion, the new node will be the first node of the linked list.

  # void addAtTail(int val) Append a node of value val as the last element of the linked list.

  # void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
  # If index equals the length of the linked list, the node will be appended to the end of the linked list. 
  # If index is greater than the length, the node will not be inserted.

  # void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
  
#first is Single linkedlist relization:
class ListNode:                         # first should build a ListNode class
    def __init__(self,x):
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):                 # need a var that record the total length of the linkedlist
        self.size = 0
        self.head = ListNode(0)         # a "fake" head built


    def get(self, index: int) -> int:
        if index<0 or index>=self.size:return -1
        cur = self.head
        for _ in range(index+1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return 
        if index<0: index = 0
        self.size += 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        temp = ListNode(val)
        temp.next = pre.next
        pre.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if index>=self.size or index<0:
            return 
        self.size -= 1
        pre = self.head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
        
