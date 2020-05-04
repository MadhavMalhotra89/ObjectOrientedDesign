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
    
  def get(self, key):
    if key in self.lru
      
    else:
      return -1
  def put(self, key, value):
    
    
  def add(self, key, value):
    if key in self.lru and self.lru[key] == value:
      return self.lru[key]
    if key in self.lru and self.lru[key] != value:
      remove(key)
      add(key, value)
      self.lru[key] = value
    elif len(self.lru) == self.capacity:
      node = self.head.next
      self._remove(node.key)
      self._add(key,value)
    else:
      self._add(key,value)
  def remove(self, key):
    temp = self.head
    while True:
      if temp.key == key:
        temp1 = temp.next
        temp2 = temp.prev
        temp.prev.next  = temp1
        temp.next.prev = temp2
        del self.lru[key]
        break
      else:
        temp = temp.next
