# import calendar

# print()

# year = 2023
# month = 7
# print(calendar.month(year, month))




class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  head = None
  pointer = -1
  
  def __init__(self):
    self.__top = None

  def push(self,elem):
    if self.head == None:
        self.head = Node(elem, None)
        self.pointer += 1
    else:
        n = Node(elem, None)
        n.next = self.head
        self.head = n
        self.pointer += 1 

  def pop(self):
    if self.head == None:
      return -99
    
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.pointer -= 1
    return temp.elem


  def peek(self):
    return (self.head.elem)

  def isEmpty(self):
    #TO DO
    pass


a = Stack()
a.push(90)
print(a.pop())
print(a.pop())