class ListNode:
    
    def __init__(self, val, prev=None, next_node=None):
        self.val = val
        self.prev = prev
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        first = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node

        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        last = self.tail.prev

        new_node.prev = last
        new_node.next = self.tail
        last.next = new_node

        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        if index == self.size:
            self.addAtTail(val)
            return None

        curr = self.head.next
      
        for _ in range(index):
            curr = curr.next
        
        new_node = ListNode(val)
        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        prev_node = curr.prev
        next_node = curr.next

        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1