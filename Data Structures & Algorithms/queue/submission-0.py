class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        old_tail = self.tail.prev
        old_tail.next = new_node
        new_node.prev = old_tail
        new_node.next = self.tail
        self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        old_head = self.head.next
        old_head.prev = new_node
        new_node.next = old_head
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popped_node = self.tail.prev
        new_tail = popped_node.prev
        new_tail.next = self.tail
        self.tail.prev = new_tail
        return popped_node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        popped_node = self.head.next
        new_head = popped_node.next
        self.head.next = new_head
        new_head.prev = self.head
        return popped_node.val
