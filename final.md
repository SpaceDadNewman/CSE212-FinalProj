# CSE 212 Final Project - Chase Wilcox

# Queues
* What are queues?

    Queues work in FIFO (First In First Out) unlike stacks that use LIFO (Last In First Out), queues are implemented within lists and have functions such as enqueue and dequeue. These operate in O(1) and therefore are incredibly efficient by themselves. 

* Example
    
    In this problem we will be implementing a list with the queue adding numbers and then taking the numbers and ensuring they are in proper numerical order by using the pop(), append(), and insert() functions.

        
        # Implementaion using a list
        myList = []
        # Adding items to the list
        myList.append(1)
        myList.append(2)
        myList.append(15)
        myList.append(3)
        myList.append(4)
        myList.append(6)
        myList.append(100)
        myList.append(9)

        print('The current queue is: ', myList)

        # Create a queue that is in proper order from 1-10

        # The pop function is removing the items at their specific index
        myList.pop(2)
        myList.pop(5)
        # The insert function is taking the index and then  putting the second value into the queue.
        myList.insert(4,5)
        myList.insert(6,7)
        myList.insert(7,8)
        # Append is just adding to the end of the list
        myList.append(10)

        print('The queue is now:', myList)

        # This will output:
        The current queue is:  [1, 2, 15, 3, 4, 6, 100, 9]
        The queue is now: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


* Problem

    There is a line of people that need to be removed from the line in FIFO order. This is the basic part of the problem. However, as the line gets shorter, every three people that have gone through the line a random person from the original line will come back into line at the end. The line has already been created [here](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/queue_problem.py). you must iterate through the line removing people and adding a random person every three people that have been removed.

* Solution

    Here is the [solution](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/queue_solution.py)

# Sets
* What are sets?
    
    Sets can store multiple values or items in a single variable. They do not allow duplicate values, they don't follow any specific order, and the items within the set cannot be changed once they've been created within the set. These typically have to iterate through multiple for loops so they are O(n^2)

* Example

        # Initialize the sets
        set1 = {"math", 25, "banana", 49, 11, "sandwich"}
        set2 = {"english", "alpha", 25, "elephant", 14}
        set3 = {"english", "jamba", 49, "lemon", 27}

        # This will combine multiple sets together using the .update() function

        settotal = set()
        for i in set1:
            for j in set2:
                for h in set3:
                    settotal.update([i,j,h])
        print(settotal)


* Problem

    Create a program that will add a list to a set and then iterate through the set and remove any numbers that are not prime numbers. Here is the initial [problem](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/set_problem.py).
    Hint: Using the sqrt function from math may prove helpful.

* Solution

    Here is the [solution](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/set_solution.py).

# Trees
* A tree consists of multiple nodes with pointers connecting them together, they can connect to multiple nodes at the same time. Starting at the base of the tree the program decides which way it should go, right or left, depending on what value it's looking for. Say there are numbers in the tree it and the base starts at 15 and it's looking for 20. It will look at the left side and determine if it's higher or lower than 15, if it's lower than 15 it will go right since it's looking for something that is higher than 15 (20). It will keep on doing this until it hits the end of the tree. This means it often operates using recursion to make it easier to work with, recursion is when you use the function within the same function to loop until it hits a base case that has been created within the class. These operate in O(n) or O(log n) if done in a balanced tree.

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