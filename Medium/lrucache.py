# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
# The cache is initialized with a positive capacity.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node:
    # each node has a key and value, if a node is pointing to the initial head node then it is the head,
    # if its pointing to the initial tail then it is the tail. If its pointing to both then it is both.
    # and it also knows its previous node and the next node after it
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class DoubleLinkedList:

    # link will look like:
    # initialheadnode = Node(None, tailnode)
    # initialtailnode = Node(headnode, None)
    def __init__(self):
        self.initialHead = Node(None, None)
        self.initialTail = Node(None, None)
        self.initialHead.next = self.initialTail
        self.initialTail.previous = self.initialHead

    # first sets the previous node of the new node to be the head node.
    # then sets the next node of the head to point to the new node.
    # then the next of the new node will be the tail and the previous of the tail will be the new node.
    # [initial head] <- [new node] -> [initial tail]
    def insert(self, node):
        node.previous, self.initialTail.previous.next = self.initialTail.previous, node
        node.next, self.initialTail.previous = self.initialTail, node

    # finds the head node. (head.next is the head node as the initial head is just a pointer to the real head)
    # points the node after the head node back to the initial head node.
    # points the initial head node to the node after the current head node.
    # get key of old head.
    # deletes the old head.
    # returns the key of the old head.
    def remove_head_node(self):
        node = self.initialHead.next
        node.next.previous = self.initialHead
        self.initialHead.next = self.initialHead.next.next
        key = node.key
        del node
        return key

    # gets the passed in nodes previous node and sets its next node to be the passed in nodes next node.
    # gets the passed in nodes next node and sets its previous node to be the passed in nodes previous node.
    # then calls the insert function on node passed in.
    def update(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        self.insert(node)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = DoubleLinkedList()
        self.mapping = {}

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self.queue.update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            self.queue.update(node)
            return

        node = Node(key, value)
        self.mapping[key] = node
        self.queue.insert(node)

        if self.capacity == 0:
            removed_key = self.queue.remove_head_node()
            del self.mapping[removed_key]
        else:
            self.capacity -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
