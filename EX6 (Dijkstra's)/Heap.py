
class Heap(object):
	# maxsize - max size of the heap
	def __init__(self, maxsize, keyfunc=lambda x: x, initval=0):
		self.max_size = maxsize
		self.size = 0
		self.arr = [0 for _ in range(self.max_size+1)]
		self.arr[0] = initval
		self.keyfunc = keyfunc
		self.index_map = {} # to store index for decrease_key
	
	# misc functions:
	def is_full(self):
		return self.size == self.max_size

	def is_empty(self):
		return self.size == 0

	# inserts one element into the heap
	def insert(self, key):
		if self.is_full():
			raise Exception('Heap Overflow!')
		
		self.size += 1
		pos = self.size

		# percolate up process
		while self.arr[pos//2] > key:
			self.arr[pos] = self.arr[pos//2]
			self.index_map[self.keyfunc(self.arr[pos//2])] = pos
			pos //= 2

		self.index_map[self.keyfunc(key)] = pos
		self.arr[pos] = key

	# to create the heap from the array in linear time
	def create_heap(self, input_arr):
		for el in input_arr:
			self.insert(el)

	# returns the smallest element in the heap in logn time
	def delete_min(self):
		if self.is_empty():
			raise Exception('Heap Underflow!')

		root, last, pos = self.arr[1], self.arr[self.size], 1
		self.size -= 1

		# percolate down
		while pos*2 < self.size:
			child = pos*2
			if self.arr[child] > self.arr[child + 1]:
				child += 1
			if last > self.arr[child]:
				self.arr[pos] = self.arr[child] 
				self.index_map[self.arr[child]] = pos 
			else:
				break
			pos = child

		# remove root
		self.arr[pos] = last
		del self.index_map[self.keyfunc(root)]

		return root 

	# function to decrease the value of a node in the heap
	def decrease_key(self, key, new_val):
		pos = self.index_map.get(key, -1)
		if pos == -1:
			raise Exception('Decrease Key Error!')
		# value update in map
		self.arr[pos] = new_val

		# percolate up again
		while self.arr[pos//2] > self.arr[pos]:
			self.arr[pos], self.arr[pos//2] = self.arr[pos//2], self.arr[pos]
			self.index_map[self.keyfunc(self.arr[pos//2])], self.index_map[self.keyfunc(self.arr[pos])] = self.index_map[self.keyfunc(self.arr[pos])], self.index_map[self.keyfunc(self.arr[pos//2])]
			pos //= 2		

	# print heap with from el as root
	def print_heap(self, depth, el):
		if self.size == 0:
			return

		print('\t' * depth + str(self.arr[el]))
		if el * 2 > self.size:
			return
		else:
			print('\t' * (depth+1)+'L  :')
			self.print_heap(depth+1, el*2)
			
			if 2*el + 1 <= self.size:
				print('\t' * (depth+1)+'R  :')
				self.print_heap(depth+1, el*2+1)
