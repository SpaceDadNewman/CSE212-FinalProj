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
	
    def insert(self, data):
        # This will start at the root
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        # if at end of tree (Base Case)
        if node.left is None and node.right is None:
            if node.data == data:
                return
        
        
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
                
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    
    # This is for the contains functions 
    
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

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)

print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False