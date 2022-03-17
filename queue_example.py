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
# The above cannot be changed

# Create a queue that is in proper order from 1-10

# The pop function is removing the items at their specific index
myList.pop(2)
myList.pop(5)
# The insert function is taking the index and then putting the second value into the queue.
myList.insert(4,5)
myList.insert(6,7)
myList.insert(7,8)
# Append is just adding to the end of the list
myList.append(10)


print('The queue is now:', myList)

