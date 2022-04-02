class BST:
	class Node:
		def __init__(self, data):
			# Intializes the note with the right data
			self.data = data
			self.left = None
			self.right = None

	def __init__(self):
		# Creates an empty BST
		self.root = None
	
	def __contains__(self, data):
		# This tells the program to start at the root
		return self._contains(data, self.root)

	def _contains(self, data, node):
		# This is the base class
		if node.data == data:
			print('True')
			return True

		else:
			# check left
			if data < node.data:
				if node.left != None:
					self._contains(data, node.left)
			# check right
			elif data > data.data:
				if node.right != None:
					self._contains(data, node.right)
			else:
				return False

# This is what will check if certain numbers are in the tree:
tree = BST()
print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
		


		

