# Python Data Structures

## Queue Tutorial

## Introduction
Python Queues are very useful in circumstances where you need to enter an item into a linear data structure that can keep ordering of items.

Another great use of queues is for performance. Queues have extremely good performance when compared to things like append and pop in a list. While looking through a list with append or pop is around O(n), a queue is typically O(1) depending on what approach you're taking with the queue.

Python queues are useful for ordered list problems. You can use a queue like a line (First-In-First_Out) where the first thing into the list is also the first thing to leave. FIFO will be covered more later. Another queue that can be utilized is a (Last-In-First-Out) where the last thing into the list is the first thing to leave. LIFO will also be covered more later.

The most common errors relating to queues are related to populating the queue and depopulating the queue. If not implemented properly, populating a queue could end up in the wrong space or the wrong index which can cause issues. When depopulating the queue, if you depopulate the wrong index, the queue might become nonfunctional or you might lose an input you needed to keep in.

### FIFO Queue Example

![FIFO_Queue](fifo_queue.png)

### LIFO Queue Example

![LIFO_Queue](lifo_queue.png)

## Building Queues
The most basic of queues would pretty much be a list. While a queue uses .enqueue() and .dequeue() for its population and depopulation, a list uses .append() and .pop(). This was referenced earlier in the performance section. While a list has O(n) performance (n being the number of items in the list), a queue has O(1) performance. This means that a list's performance is dependant on how long it is and a queue keeps the same performance no matter the length.

```python 
# This is a simple list queue

# Define or initialize the list
queue = []

# Add things to the queue
queue.append('z')
queue.append('y')
queue.append('x')

print('First queue')
print(queue)

# Remove stuff from the queue
print('Items dropped from queue')
print()
print(queue.pop(0))
print(queue.pop(0))

print()
print('Items left in queue')
print(queue)
```
Output:

First queue

['z', 'y', 'x']

Items dropped from queue        

z

y

Items left in queue

['x']

As you can see, using a list and .pop(0) removes the first element in the queue. When we popped two things out of the queue, 'z' was removed first, 'y' was removed second, and 'x' was not removed because we only popped out two things. Now that we have a FIFO queue built from a list, we'll build a FIFO queue in a queue.

- `queue = []` - Initializes a list

- `.append(x)` - Adds x item to the list

- `.pop(0)` - Pops out the last item in the list

## Build a FIFO Queue Using Queue Module (First-In_Last_Out)
The easiest way to make a queue in Python would be to use the Queue built-in module. This allows you to use knowledge from the list data structure but still have the performance that queues offer. To implement this we will be building a FIFO queue using the Queue module. We will use multiple functions listed below the example code to build this queue. This queue does have a maxsize constraint so if you want something without a maxsize constraint you can use 'queue.SimpleQueue()'.

```python 
# This is a simple FIFO queue

# Import queue from Queue to use queue functions
from queue import Queue

# Define the maxsize of the queue and intitialize it
Q = Queue(maxsize = 5)
# If wanting a queue with no maxsize
from queue import SimpleQueue
Q = queue.SimpleQueue
# Print the size of the queue (Should be at 0 as we have not put anything in it)

# Blank line for spacing
print()

size = (Q.qsize())
print(f'Queue size: {size} ')

# Check if the queue is empty (Should return True)
empty = (Q.empty())
print(f"Queue is empty: {empty} ")

# Blank line for spacing
print()

# Add things to the queue
Q.put('z')
print(f'Added "z" to the queue. ')
Q.put('y')
print(f'Added "y" to the queue. ')
Q.put('x')
print(f'Added "x" to the queue. ')

# Blank line for spacing
print()

# Print the new size of the queue (Should be at 3 as we have put 3 items in it)
size = (Q.qsize())
print(f'Queue size: {size} ')

# Check is the queue is empty (Should return False now)
empty = (Q.empty())
print(f"Queue is empty: {empty} ")

# Blank line for spacing
print()

# Add a couple more things to the queue
Q.put('w')
print(f'Added "w" to the queue. ')
Q.put('v')
print(f'Added "v" to the queue. ')

# Blank line for spacing
print()

# Check queue size again
size = (Q.qsize())
print(f'Queue size: {size} ')

# Is the queue full?
full = (Q.full())
print(f'Queue is full: {full}') 

# Blank line for spacing
print()

# Remove elements from queue in FIFO
print(f'Elements dequeued: ')
print(Q.get())
print(Q.get())
print(Q.get())

# Blank line for spacing
print()

# Check if full again
full = (Q.full())
print(f'Queue is full: {full}') 

# Blank line for spacing
print()

# Check queue size after dropping 3 elements (Should be 2)
size = (Q.qsize())
print(f'Queue size: {size} ')

# Blank line for spacing
print()

# Dequeue the rest
print(f'Elements dequeued: ')
print(Q.get())
print(Q.get())

# Blank line for spacing
print()

# Check is the queue is empty (Should return True now)
empty = (Q.empty())
print(f"Queue is empty: {empty} ")

```
Output:

Queue size: 0 

Queue is empty: True

Added "z" to the queue.

Added "y" to the queue.

Added "x" to the queue.

Queue size: 0

Queue is empty: False

Added "w" to the queue.

Added "v" to the queue.

Queue size: 5

Queue is full: True

Elements dequeued:

z

y

x

Queue is full: False

Queue size: 2

Elements dequeued:

w

v

Queue is empty: True

- `Queue(maxsize = x)` - Initializes a queue with (x) maxsize

- `.qsize()` - Returns the size of the queue

- `.empty()` - Returns a boolean if a queue is empty or not

- `.full()` - Returns a boolean if a queue is full or not

- `.put(x)` - Puts x item into a queue

- `.get()` - Dequeues item from queue

## Build a LIFO Queue Using Queue Module (Last-In-First-Out)
Luckily, using the queue module helps us considerably when building a LIFO queue. This lets us use all the same things as earlier in the FIFO queue but just automatically changes it to LIFO. Normally a LIFO queue would include recursion or some odd forms of list ordering. queue.LifoQueue() allows us to use all the knowledge gathered from the FIFO queue and just implement it automatically into the LIFO queue. This tutorial will be a bit shorter because it's the same concepts reused.

```python 
# This is a simple LIFO queue

# Import queue from Queue to use queue functions
from queue import LifoQueue

# Define the maxsize of the queue and intitialize it
Q = LifoQueue(maxsize = 5)

# Check if queue is empty
empty = (Q.empty())
print(f"Queue is empty: {empty} ")

# Blank line for spacing
print()

# Queue elements
Q.put('a')
Q.put('b')
Q.put('c')
Q.put('d')
Q.put('e')

full = (Q.full())
print(f"Queue is full: {full} ")
print()
print(f'Elements dequeued: ')
print(Q.get())

```
As you can see in this example, the final output, 'e' is the last thing dequeued. You can also see that e was the last thing that was entered into the queue. Therefore, this queue is LIFO. The last thing in was the first thing out.

Output:

Queue is empty: True

Queue is full: True

Elements dequeued:

e

## Problem to Solve: FIFO with names

Write a program that builds a FIFO queue that utilizes names and their order. Use the following names, 'Bob', 'Sue', 'Jeff'.

Make a program where Bob comes first in the queue, is used twice, then placed behind Jeff. Sue should come after the second Bob then utilize Jeff 3 times before Bob comes again. The queue should have a maxsize of 5 so that Bob is forced to be recycled. Without the maxsize constraint you could just add Bob to the end instead of ordering it properly. When adding items to the list, make sure you are filling it up before removing anything (queue.full?). At the end make sure to verify the queue is empty as well. When you remove items from the queue make sure you are using the print([your funtion here]) so that you can see the names when they are taken out. The order they should be in is: 

- [Order Spoiler If Stuck](order.md)

Try your best to work through the solution before looking at it below. Everything in this problem has been covered above so if you get stuck try reading through the material again first.

- [Solution](1-solution.py)

- [Back to Welcome Page](1-1-Introduction.md)