// https://leetcode.com/problems/lru-cache

'''solution using ordered dictionary of python'''
# import collections
# class LRUCache(collections.OrderedDict):

#     def __init__(self, capacity: int):
#         self.size = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         else:
#             self.move_to_end(key)
#             return self[key]

#     def put(self, key: int, value: int) -> None:
#         self[key] = value
#         self.move_to_end(key)
#         if len(self) > self.size:
#             self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DLNode:
    
    def __init__(self):
        self.value = 0
        self.key = 0
        self.left = None
        self.right = None

class LRUCache:
    
    def __init__(self, max_size):
        self.dict = {}
        self.max_size = max_size
        self.size = 0
        self.head = DLNode()
        self.tail = DLNode()
        self.head.right = self.tail
        self.tail.left = self.head
    
    def push_to_head(self, node):
        node.left = self.head
        self.head.right.left = node
        node.right = self.head.right
        self.head.right = node
    
    def move_to_head(self, node):
        node.left.right = node.right
        node.right.left = node.left
        
        node.right = self.head.right
        self.head.right = node
        node.left = self.head
        node.right.left = node
        
    def pop_tail(self):
        key = self.tail.left.key
        self.tail.left = self.tail.left.left
        self.tail.left.right = self.tail
        del self.dict[key]
    
    def get(self,key):
        if key in self.dict:
            val = self.dict[key].value
            self.move_to_head(self.dict[key])
            return val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.dict:
            self.dict[key].value = value
        elif self.size < self.max_size:
            self.size += 1
            self.dict[key] = DLNode()
            self.dict[key].value = value
            self.dict[key].key = key
            self.push_to_head(self.dict[key])
        else:
            self.pop_tail()
            self.dict[key] = DLNode()
            self.dict[key].value = value
            self.dict[key].key = key
            self.push_to_head(self.dict[key])
        
        
        
        
        
        
        
        
        
        
        
        
        
        