from queue import Queue
# Initialize Queue
line = Queue(maxsize = 5)

# Verify the queue is empty
empty = (line.empty())
print(f"Queue is empty: {empty} ")
print()
name1 = 'Bob'
name2 = 'Sue'
name3 = 'Jeff'

line.put(name1)
line.put(name1)
line.put(name2)
line.put(name3)
line.put(name3)

# Verify the queue has 5 items
number = (line.qsize())
print(f'The queue has "{number}" items in it. ')
print()

# Verify the queue is full
full = (line.full())
print(f"Queue is full: {full} ")
print()

# Get the first Bob out
print(line.get())
print()

# Verify the queue has 4 items
number = (line.qsize())
print(f'The queue has "{number}" items in it. ')
print()
## Put the third Jeff in
line.put(name3)

# Verify the queue is full
full = (line.full())
print(f"Queue is full: {full} ")
print()
# Get the second Bob out
print(line.get())
print()
# Verify the queue has 4 items
number = (line.qsize())
print(f'The queue has "{number}" items in it. ')
print()
# Put the last Bob
line.put(name1)

# Verify the queue is full
full = (line.full())
print(f"Queue is empty: {full} ")
print()
# Get the remaining items
print(line.get())
print()
print(line.get())
print()
print(line.get())
print()
print(line.get())
print()
print(line.get())
print()

# Verify the queue is empty
empty = (line.empty())
print(f"Queue is empty: {empty} ")