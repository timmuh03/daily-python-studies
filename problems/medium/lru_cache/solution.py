"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, 
evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""



class LRUNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next: LRUNode | None = None
        self.prev: LRUNode | None = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.nodes: dict[int, LRUNode] = {}

        self.head: LRUNode = LRUNode(-1, -1)
        self.tail: LRUNode = LRUNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _to_front(self, node: LRUNode) -> None:
        assert node.next is None and node.prev is None
        old_first = self.head.next; assert old_first is not None
        old_first.prev = node
        self.head.next = node
        node.next = old_first
        node.prev = self.head


    def _detach(self, node: LRUNode) -> None:
        prev = node.prev; assert prev is not None
        next = node.next; assert next is not None
        prev.next = next
        next.prev = prev

        node.next = node.prev = None
        

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]

            self._detach(node)
            self._to_front(node)
            
            return node.value
        
        return -1


    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            node = LRUNode(key, value)
            self.nodes[key] = node
            while len(self.nodes) > self.capacity:
                old_last = self.tail.prev; assert old_last is not None
                old_key = old_last.key
                self._detach(old_last)

                del self.nodes[old_key]
                del old_last
                
                
            self._to_front(node)
        else:
            node = self.nodes[key]
            node.value = value
            self._detach(node)
            self._to_front(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)