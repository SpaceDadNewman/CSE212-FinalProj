import random
queue = []

queue.append('John')
queue.append('Jacob')
queue.append('Jinkleheimer')
queue.append('Schmidt')
queue.append('Michael')
queue.append('Abby')
queue.append('Morgan')
queue.append('Madelyn')
queue.append('Ashley')
queue.append('Lucy')
# Above cannont be changed

print(queue)
# this creates a copy of the queue
originalQueue = queue.copy()
count = 0

# this does all the work
while len(queue) != 0:
    # removes the first item in the list
    queue.pop(0)
    # adds one to the count
    count += 1
    print(queue)
    # once the count hits three the count will reset and then add a random person from the original queue into queue
    if count == 3:
        count = 0
        queue.insert(len(queue), random.choice(originalQueue))

