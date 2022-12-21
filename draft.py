# Import the Node class
from binarytree import Node

root = Node(1)                  # index: 0, value: 1
root.left = Node(2)             # index: 1, value: 2
root.right = Node(3)            # index: 2, value: 3
root.left.right = Node(4)       # index: 4, value: 4
root.left.right.left = Node(5)  # index: 9, value: 5

# Print the tree
print('Base tree:')
print(root)
print()

# Print a specific node according to index

print(f'Index 2: {root[2]}')
print()

# Print the tree + the index
print('Tree 2 (Printed tree with index values): ')
root.pprint(index=True)
print()

# Replace a specific node according to index
root[4] = Node(6, left=Node(7), right=Node(8))
print('Tree 3 (Changed 6th node and appended two values): ')
root.pprint(index=True)
print()

# Delete a node according to index
print('Tree 4 (No 6th Node): ')
del root[4]
root.pprint(index=True)
print()