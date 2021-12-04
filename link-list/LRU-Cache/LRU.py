#trick of declaring a double link list:
#   Leave head and tail as empty node will be helpful when inserting and deletion
#   Be careful when the key is repeated.
class ListNode:
    def __init__(self, value = None, key = None):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def addNode(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
    def delNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node.key
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.delNode(node)
        self.addNode(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.delNode(node)
            self.addNode(node)
        elif len(self.map) < self.capacity:
            node = ListNode(value, key)
            self.map[key] = node
            self.addNode(node)
        else:
            delkey = self.delNode(self.head.next)
            self.map.pop(delkey)
            node = ListNode(value, key)
            self.map[key] = node
            self.addNode(node)
            