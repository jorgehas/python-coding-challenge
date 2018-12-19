'''
Author: Georges Hassana
12/19/2018

Description:
 write a new Geo Distributed LRU (Least Recently Used) cache with
 time expiration.

 Requirements:
	1 - Simplicity. Integration needs to be dead simple.
    2 - Resilient to network failures or crashes.
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.
    4 - Data consistency across regions
    5 - Locality of reference, data should almost always be available from the closest region
    6 - Flexible Schema
    7 - Cache can expire	
'''
import time

#Define a class Node that will enable access to the cache contents
class Node(object):

	def __init__(self,key, value, time):
		self.key = key
		self.value = value
		self.time = time
		self.previous = None
		self.next = None
#Define a class LinkedList
class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def __insertitem__(self,node):
		node.next = None 
		node.previous = None
		if self.head is None:
			self.head = node
		else:
			self.tail,next = node
			self.previous = self.tail
		self.tail = node

	def __removeitem__(self,node):
		if node.previous:
			node.previous.next = node.next
		else:
			self.head = node.next
		if node.next:
			node.next.previous = node.previous
		else:
			self.tail = node.previous
		node.next = None
		node.previous = None


class LRUCache:
	def __init__(self, size):
		self.list = LinkedList()
		self.size = size
		self.cache = {}
		cur_time = time.time()

		#expiry time
		self.expiry_time = 30

	def __setitem__(self, key, value):
        # .
        if key in self.cache:
            node = self.cache[key]

            # Replace the value.
            node.value = value

            # Update the list ordering.
            self.mtf(node)
            self.head = node

	def __additem__(self,key,value):
		node = Node(key, value, cur_time)
		self.list.__insertitem__(node)
		self.cache[key] = node
		cur_time = time.time()


	def put(self,key,value):
		
		if key in self.cache:
			self.list.__removeitem__(self.cache[key])

		elif len(self.cache) == self.size:
			del self.cache[self.list.head.key]
			self.list.__removeitem__(self.list.head)

		self._additem__(key,value)

	def get(self,key,value):

		cur_time = time.time()
		if key in self.cache:
			node = self.cache[key]
			self.cache[key].time = cur_time

		self.__removeitem__(node)
		sel.__insertitem__(node)
		return node.value

	def _remove_expiredNode():
		
		if key in self.cache:
			node = self.cache[key]
			if cur_time - node.time > self.expiry_time:
				self.__removeitem__(node)
				del self.cache[node.key]



if __name__ == "__main__":
    cache = LRUCache(3,3,30)
    cache.__setitem__(1, 1, 10)
    cache.__setitem__(2, 2, 9)
    print(cache.get(3,3,20))
	



