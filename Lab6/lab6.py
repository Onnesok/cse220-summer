######################### Question 1 ################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@  1A  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def fact(n):
  if n == 1:
    return 1
  else:
    return n*fact(n-1)
print("Factorial: ",fact(4))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  1B  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def fibonacci(n):
  if n <= 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci: ",fibonacci(4))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  1C  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def arr(a, i, n):
  if i == n:
    return
  else:
    print(a[i])
    return arr(a, i+1, n)
  
arr([1,2,5,4,10], 0, 5)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  1D  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def power(a, n):
  if n ==0:
    return 1
  else:
    return a * power(a, n-1)

print("power: ",power(3,3))

################################ Task 2  ###############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2A   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def binary(n):
  rem = n%2
  if n == 0:
    return ""
  else:
    return binary(n//2) + str(rem)
print("Binary number: ",binary(20))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2B   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import math
  
class Sum:
    tsum = None
  
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
  
def push(head, data):
    if not head:
        return Node(data)
   
    new_node = Node(data)
  
    new_node.next = head
  
    head = new_node
    return head
  
# linked list 
def sumOfNode(head, S):
      
    # if head = NULL
    if not head:
        return
      
    sumOfNode(head.next, S)
      
    S.tsum += head.data 


def sumOfNodesUtil(head):
    S = Sum()
    S.tsum = 0
      
    sumOfNode(head, S)
      
    return S.tsum
  

head = None

head = push(head, 1)
head = push(head, 2)
head = push(head, 3)
head = push(head, 5)
head = push(head, 4)
print("Sum of Nodes = ", sumOfNodesUtil(head))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  2C @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Node:
  def __init__(self, element, n):
    self.element = element
    self.next = n

class LinkedList:
  def __init__(self, a):
    self.head = None 
    if type(a) == list:
      for i in range(0,len(a)):
        newNode = Node(a[i],None)
        if (self.head == None):
          self.head = newNode
          tail = newNode
        else:
          tail.next = newNode
          tail = newNode
    if type(a)==Node:
      self.head = a

  def reverseList(self,h):
    if h == None:
      return
    else:
      self.reverseList(h.next)
      print(h.element)

a = [10,20,30,40]
h1 = LinkedList(a)
(h1.reverseList(h1.head))

###############################  Task 3  ###############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  3  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def hocBuilder(h):
  if h == 0:
    return 0
  elif h == 1:
    return 8
  else:
    return 5+hocBuilder(h-1)


print("HocBuilder: ",hocBuilder(2))

###############################  Task 4  ###############################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  4A  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def num(i, n):
  if i == n+1:
    print()
    return
  print(i, end=" ")
  i = i+1
  return num(i, n)

def pattern(a, i):
  if i == a+1:
    return
  num(1, i)
  pattern(a, i+1)

#F call
pattern(5, 1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  4B  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def forward(i, n):
  if i == n+1:
    print()
    return
  print(i, end=" ")
  i = i+1
  return forward(i, n)

def num(a, i, j):
  if i == j-1:
    return
  print(" ", end=" ")
  i = i-1
  return num(a, i, j)

def pattern(a, i):
  if i == a:
    return
  num(a, a-i, 1)
  forward(1, i)
  pattern(a, i+1)
  if i == a-1:
      forward(1, i+1)
#F call
pattern(5, 1)

###############################  Task 5  ###############################

class FinalQ:
  def printt(self,array,idx):
    if idx<len(array):
      profit = self.calcProfit(array[idx])
      print("{}. Investment: {}; Profit: {}".format(idx + 1, array[idx], self.calcProfit(array[idx])))
      self.printt(array,idx+1)

  def calcProfit(self,investmentt):
    if investmentt == 25000:
      return 0.0
    else:
      if investmentt<=100000:
        return self.calcProfit(investmentt-1000)+45.0
      else:
        return self.calcProfit(investmentt-1000)+80.0

array = [25000,100000,250000,350000]
f = FinalQ()
f.printt(array,0)

# Recursion