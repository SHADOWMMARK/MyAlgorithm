"""
use two pointers, one moves one step at a time, the other moves two steps at a time
"""

def hasCycle(head) -> bool:
    if not head:
        return False
    low, high = head,head
    while high.next and high.next.next:
        low = low.next
        high = high.next
        high = high.next
        if low == high:
            return True
    return False