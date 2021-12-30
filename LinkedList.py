class Node():
  def __init__(self, data):
    self.data = data;
    self.next = None;

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.next = b
b.next = c
c.next = d
d.next = e

# Iterative traversal of Linked List
def TraverseIter(head):
  current = head
  while (current != None):
    print(current.data)
    current = current.next


# Recursive traversal of Linked List
def TraverseRecur(head):
  if (head == None):
    return
  print(head.data)
  TraverseRecur(head.next)


# Searching through a Linked List (iteratively)
def Search(target, head):
  current = head
  while (current != None):
    if (current.data == target):
      return True
    current = current.next




# Searching through a Linked List (recursively)
def SearchRecursive(target, head):
  if (head == None):
    return False
  if (head.data == target):
    return True
  SearchRecursive(target, head.next)


# Sum of Linked List (recursively)
def SumListRecursive(head):
  if (head == None):
    return 0
  return head.data + SumListRecursive(head.next)
  
# Sum of Linked List (iterably)
def SumListItter(head):
  sum = 0
  current = head
  while (current != None):
    sum += current.data
    current = current.next

# Value of Node based on its position

## Recursive solution
def ValNodeRecursive(position, head):
  if (head == None):
    return
  if position == 0:
    return head.data
  return ValNodeRecursive(position - 1, head.next)

## Iterative solution
def ValNodeIterative(position, head):
  current = head
  while (position > 0):
    current = current.next
    position -= 1
  return current.data


# Reversing a linked list

## Recursive solution
def ReverseRecursive(head, previous = None):
  if (head == None):
    return previous
  next = head.next
  head.next = previous
  return ReverseRecursive(next, head)
  
  
## Iterative solution

def ReverseIterative(head):
  current = head
  previous = None
  while (current != None):
    next = current.next
    current.next = previous
    previous = current
    current = next
  return previous


# Zipper List

