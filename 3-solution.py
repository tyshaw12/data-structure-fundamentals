# Import the Node class
from binarytree import Node

root = Node(1)                  
root.left = Node(2)             
root.right = Node(3)            
root.left.right = Node(4)     
root.left.left = Node(2)   
root.left.left.left = Node(1)
root.left.left.right = Node(8)

root.left.right.left = Node(5)  

# Print the tree
print('Base tree:')
root.pprint(index=True)
print()

# Replace Index 7 with 6, old 1, and add two nodes
root[7] = Node(6, left=Node(7), right=Node(8))
print(f' Tree after replacing index 7: ')
root.pprint(index=True)
print()

# Delete Index 8
del root[8]
print(f' Tree after deleting 8: ')
root.pprint(index=True)
print()
