from math import sqrt

numbers = {25,11,6,3,1,4}
morenumbers = [27,9,4,19,8,5]
# The above can not be changed


# Adds the list 'morenumbers' to 'numbers'
numbers.update(morenumbers)
# Creates a list of non prime numbers to remove
numbersremove = []

# Iterates through the set and checks if they are prime and adds to the remove list
for n in numbers:
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            numbersremove.append(n)

# Removes the numbers from the previous loop
for n in numbersremove:
    numbers.remove(n)

print(numbers)