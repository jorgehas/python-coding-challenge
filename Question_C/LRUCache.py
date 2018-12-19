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
	def __insert__(self,node):
		node.next = None 
		node.previous = None


class LRUCache:
	def __init__(self, size):
		cur_time = time.time()
		self.size = size
		 










