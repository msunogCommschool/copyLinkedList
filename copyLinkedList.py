# Copy Linked List


class Node:
	def __init__(self, val, next, rand):
		self.val = val
		self.next = next
		self.rand = rand

class LinkedList:
	def __init__(self, first):
		self.first = first
		self.last = first

	def addNode(self, val, rand):
		new = Node(val, None, rand)

		(self.last).next = new
		self.last = new


# Returns the first node of a copy of the linked list starting at the given node
# Node -> Node
def copyList(first):
	
	node = first
	copyList = LinkedList(node)
	node = first.next
	
	while node != None:
		copyList.addNode(node.val, node.rand)
		node = node.next

	return copyList.first

# Testing
d = Node("d", None, None)
c = Node("c", d, d)
b = Node("b", c, d)
a = Node("a", b, b)

testList = LinkedList(a)

# Prints out the values and random nodes' values of a linked list in order
# Node ->
def printLinkedList(first):
	node = first
	while node != None:
		if (node.rand) == None:
			print("value: " + node.val + " random's value: None")
		else:
			print("value: " + node.val + " random's value: " + (node.rand).val)
		node = node.next




