from typing import List

class LinkedListNode:
    def __init__(self, data: int = 0, next: 'LinkedListNode' | None = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        # self.head is a dummy node. Real data starts at self.head.next
        self.head = LinkedListNode()
        self.tail = self.head
        self.count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        
        # Start at the first actual data node
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.data

    def insertHead(self, val: int) -> None:
        new_node = LinkedListNode(val, self.head.next)
        self.head.next = new_node
        
        # If the list was empty, this new node is also the tail
        if self.tail == self.head:
            self.tail = new_node
            
        self.count += 1

    def insertTail(self, val: int) -> None:
        new_node = LinkedListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.count:
            return False
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        if prev.next == self.tail:
            self.tail = prev

        prev.next = prev.next.next
        self.count -= 1
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals.append(curr.data)
            curr = curr.next
        return vals
