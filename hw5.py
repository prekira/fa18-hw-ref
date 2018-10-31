"""
Class for linked list node.
"""
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

"""
Will print the linked list for you.
Input:
	head - the head of the linked list.
"""

def print_list(head):
	while head:
		print(str(head.data) + "->")
		head = head.next_node

def get_size(head):
	counter = 0
	current_node = head
	while current_node != None:
		counter += 1
		current_node = current_node.next_node
	return counter
	pass

'''
nodex.next_node = Node(2, None)
nodex.next_node.next_node = Node(3, None)
nodex.next_node.next_node.next_node = Node(4, None)
nodex.next_node.next_node.next_node.next_node = Node(5, None)
'''

"""
The input and output examples that are provided in this homework will be drawn as follows:
Example: a -> b -> c
This means that the node who's data is 'a' has a next_node whose data is 'b'. And so forth.
Note, that the 'head' input for the following problems is of type 'Node'.


Hint: multiple nodes can hold the same data. So, be careful when comparing nodes.
"""



"""
Given the head of a linked list, insert the data at the given position
Note: The head is at position 0.

If the insertion index is not valid (too large or too small) simply return the original head.
Input:
	head - the head of the linked list.
	data - the item to add to the head of the linked list.
	position - position to insert
	
Output: 
	Return the head of the resulting linked list

Example:
	Input: 
		a -> c -> d -> e, 'b', 1
	Output:
		a -> b -> c -> d -> e

Example 2:
	Input:
		b -> c -> d -> e, 'a', 0
	Output:
		a -> b -> c -> d -> e

"""

def add_position(head, data, position):
	parent_node = head
	if head is None:
		return None
	if data is None:
		return None
	size = get_size(head)
	#if position < 0 or self
	if position < 0 or position > size:
		return None
	current_node = head
	if position == 0:
		newnode = Node(data, parent_node)
		return parent_node
	position -= 1
	pos_count = 0
	print("data = ", data, "position=",position)
	while pos_count < position:
		if current_node.next_node == None:
			break
		current_node = current_node.next_node
		print("count = ", pos_count, "current_node= ", current_node.data) 
		pos_count += 1
	node_at_pos = current_node.next_node
	current_node.next_node = Node(data)
	current_node = current_node.next_node
	current_node.next_node = node_at_pos
	print(print_list(head))
	return parent_node
	pass
"""
Given the head of a linked list and a position, remove the node at the given position.
Note: the head is at position 0. 

If the remove index is invalid (too small or too large) simply return the head of the orignal linked list.

Input:
	head - the head of the linked list.
	position - the position to remove
Output:
	the head of the resulting linked list

Example:
	Input:
		a -> b -> c -> d -> e, 2
	Output:
		a -> b -> d -> e
"""
def remove_position(head, position):
	pass


"""
Given the head of two linked lists, returns the data at the merge point.
Returns None if they do not merge.
Input:
	head_a: head of the first linked list
	head_b: head of the second linked list
output:
	the data of the merge node
Example:
Input:	
	a -> b -> c -> d, f -> c -> d
Output:
	'c'

Example 2:
Input:
	a -> b -> c -> d, e -> f -> g
Output:
	None
"""
def find_merge_point(head_a, head_b):
	pass

"""
Given the head of a linked list, determines whether or not there
is a cycle in the linked list.

Input:
	head - the head of the linked list.
	
Output:
	(bool) whether or not there is a cycle in the linked list.
Example:
	Input:
		a -> b -> c -> d -> e -> f -> g -> b (And so forth)
	Output:
		TRUE
"""
def find_cycle(head):
	pass

"""
Given the head of a linked list, reverse the linked list.

Input:
	head - The head of the linked list
Output:
	The head of the new linked list

Example:
	Input:
		a -> b -> c -> d -> e
	Output:
		e -> d -> c -> b -> a
"""
def reverse_list(head):
	pass


"""
Given the head of two sorted linked lists, merge them to form 1 sorted linked list.

Input:
	head_a - head of the first linked list
	head_b - the head of the second linked list
Output:
	the head of the merged sorted linked list

Example:
	Input:
		1 -> 3 -> 5 -> 7
		2 -> 4 -> 6 -> 8
	Output:
		1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
"""
def merge_lists(head_a, head_b):
	pass


#tester
list_x = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

list_x.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5

list_x = add_position(list_x, 20, 3)
'''
list_x.add(node2)
list_x.add(node3)
list_x.add(node4)
list_x.add(node5)
'''

print(get_size(list_x))
print(print_list(list_x))