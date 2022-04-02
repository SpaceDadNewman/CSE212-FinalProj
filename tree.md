# Trees
* What are trees?

    A tree consists of multiple nodes with pointers connecting them together, they can connect to multiple nodes at the same time. Starting at the base of the tree the program decides which way it should go, right or left, depending on what value it's looking for. Say there are numbers in the tree it and the base starts at 15 and it's looking for 20. It will look at the left side and determine if it's higher or lower than 15, if it's lower than 15 it will go right since it's looking for something that is higher than 15 (20). It will keep on doing this until it hits the end of the tree. This means it often operates using recursion to make it easier to work with, recursion is when you use the function within the same function to loop until it hits a base case that has been created within the class. These operate in O(n) or O(log n) if done in a balanced tree.

* Example

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
        print(3 in tree)
        print(2 in tree)
        print(7 in tree)
        print(6 in tree)
        print(9 in tree)


* Problem

    Using the above example create an insert function that will add numbers to the tree so that the example will actually work.

* Solution

    Here is the [solution](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/tree_solution.py)