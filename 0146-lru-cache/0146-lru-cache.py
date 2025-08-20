class Node:
    def __init__(self,key:int,value:int):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}       #key ->  value

        self.head=Node(-1,-1)       #dummy
        self.tail=Node(-1,-1)        #dummy
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def add_node(self,node):
        temp=self.head.next   # We do this so we don’t lose track of the old first node.(A)
        node.next=temp     #new node (X) now points forward to (A).
        node.prev=self.head
        
        self.head.next=node
        temp.prev=node

    def remove_node(self,node):
        prev=node.prev      #Remember the neighbors (prev and nxt).
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]        #Since this key was just accessed, it becomes the most recently used:
        self.remove_node(node)
        self.add_node(node)
        self.cache[key]=node
        return node.value

    def put(self,key:int,value:int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.remove_node(node)
            del self.cache[key]
        
        if len(self.cache)==self.capacity:
            lru=self.tail.prev
            self.remove_node(lru)
            del self.cache[lru.key]

        new_node=Node(key,value)
        self.add_node(new_node)
        self.cache[key]=new_node
"""
If not found → return -1.

If found → move it to front (mark most recent), return its value.

Time complexity = O(1).
"""




    
"""If the key already exists:

Remove the old node from the list (remove_node)

Delete its entry from the dictionary
We do this so we can insert the updated key-value pair as most
 recent.
 
If cache is full:

Find the least recently used node → it’s the one just before the dummy tail.

Remove it from the list and delete it from dictionary.

This frees space for the new key.
 """






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)