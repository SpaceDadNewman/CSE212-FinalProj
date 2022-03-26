# Sets
* What are sets?
    
    Sets can store multiple values or items in a single variable. They do not allow duplicate values, they don't follow any specific order, and the items within the set cannot be changed once they've been created within the set.

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