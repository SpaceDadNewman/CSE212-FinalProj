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

        This will output:
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
* What are trees?

* Example

* Problem

* Solution

    Here is the [solution](https://github.com/SpaceDadNewman/CSE212-FinalProj/blob/main/tree_solution.py)