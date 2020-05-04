Class LinkedList:
  def __init__(self, key, val):
    self.val = val
    self.key = key
    self.next = None
    self.prev = None

Class LRU:
  def __init__(self, capacity):
    self.capacity = capacity
    self.lru = {}
    self.head = LinkedList(0, 0)
    self.tail = LinkedList(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head
