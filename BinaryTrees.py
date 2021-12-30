class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       a
#      / \
#     b   c
#   /  \   \
# d     e   f

# Traversing through a binary tree
# Depth first values

### Iterative solution
def depthFirstValueI(root):
  if (root == None):
    return
  stack = [root]
  while (stack):
    current = stack.pop()
    print(current.data)
    if (current.right):
      stack.append(current.right)
    if (current.left):
      stack.append(current.left)

### Recursive solution    
def depthFirstValueR(root):
  if (root == None):
    return []
  leftValues = depthFirstValueR(root.left)
  rightValues = depthFirstValueR(root.right)

  return [root.data] + leftValues + rightValues

# Breadth first values

## Iterative solution is only posible since it requires the use of queue

def breadthFirstValue(root):
  if root == None:
    return []
  queue = [root]
  while (queue):
    current = queue.pop(0)
    print(current.data)
    if current.left != None:
      queue.append(current.left)
    if current.right != None:
      queue.append(current.right)
  