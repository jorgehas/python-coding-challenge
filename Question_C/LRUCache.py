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
Example: 
'''
import time

#Define a class Node that with enable access to the cache contents
class Node(object):

	def __init__(self,key, value, time):
		self.key = key
		self.value = value
		self.time = time
		self.previous = None
		self.next = None

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
		cur_time = time.time()
		self.list = LinkedList()
		self.size = size
		self.dict = {}

	def _add(self,key,value):
		node = Node(key,value)
		self.list.__insertitem__(node)
		self.dict[key] = node

	def put():
		if key in self.dict:
			self.list.__removeitem__(self.dict[key])

		elif len(self.dict) == self.size:
			

	








