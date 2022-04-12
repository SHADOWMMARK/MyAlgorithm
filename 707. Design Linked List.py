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
        
## double linkedlist will be more quick but need to make the "fake" head and tail, also need to record the lenght

class ListNode:                         # first should build a ListNode class 
    def __init__(self,x):
        self.val = x
        self.next = None                # double linkedlist having both prev and next
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1
        
        # choose the fastest way: to move from the head
        # or to move from the tail
        if index < self.size//2:                        ##!!! this is why use double linked list is 2 times fast then single linked list, this will save half
            curr = self.head                                # by deciding wether to search from the head or the tail
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
                
        return curr.val
            

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

        # If index is greater than the length, 
        # the node will not be inserted.
        if index>self.size:
            return
        # [so weird] If index is negative, 
        # the node will be inserted at the head of the list.
        if index<0:
            index = 0

        
        # find predecessor and successor of the node to be added
        if index<self.size//2:
            pre = self.head
            for _ in range(index):
                pre = pre.next
            succ = pre.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pre = succ.prev
        # insertion itself
        add = ListNode(val)
        add.prev = pre
        add.next = succ
        pre.next = add
        succ.prev = add
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return
        
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred
