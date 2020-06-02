
from Heap import Heap

# test class
class HeapDemo(object):

	def __init__(self, arr):
		heap = Heap(len(arr))
		heap.create_heap(arr)
		heap.print_heap(0, 1)


def main():
	HeapDemo(list(map(int, input('Enter array to print as heap: ').split())))

if __name__ == '__main__':
	main()
