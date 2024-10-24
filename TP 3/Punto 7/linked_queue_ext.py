from data_structures import ListNode
from typing import Optional

class LinkedQueueExt():
    
    def __init__(self):
        self.front: Optional[ListNode] = None
        self.rear: Optional[ListNode] = None
        self.size: int = 0

    def enqueue(self, item):
        new_node = ListNode(item)
        
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        
        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if not self.front:
            return None
        
        removed_item = self.front.element
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
        self.size -= 1
        
        return removed_item

    def is_empty(self):
        return self.size == 0