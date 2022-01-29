class Node:
  def __init__(self, data, next_node=None):
    self.data = data
    self.next = next_node

def make_linked_list(theList):
    head = Node(theList[0], None)
    current = head
    for i in range(1, len(theList)):
        newNode = Node(theList[i], None)
        current.next = newNode
        current = current.next
    return head

def printList(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next

def reverse_linked_list(linked_list):
  current = linked_list
  newHead = Node(current.data, None)
  current = current.next
  while current != None:
    newNode = Node(current.data, newHead)
    newHead = newNode
    current = current.next

  return newHead

newList = make_linked_list([4,8,15])
print("Original")
printList(newList)
reverseList = reverse_linked_list(newList)
print("Reversed")
printList(reverseList)
