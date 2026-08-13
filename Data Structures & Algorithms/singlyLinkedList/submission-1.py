class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1
            

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if self.tail == self.head:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr.next and i < index:
            curr = curr.next
            i += 1

        if curr.next is None:
            return False
        
        node_to_remove = curr.next

        if node_to_remove == self.tail:
            self.tail = curr
        
        curr.next = node_to_remove.next
        return True

    def getValues(self) -> List[int]:
        output = []
        curr = self.head.next
        while curr:
            output.append(curr.val)
            curr = curr.next
        return output
