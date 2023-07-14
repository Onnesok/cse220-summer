# ############################################################ Task 2  #############################################
# ##### Using linked list based stack
# class Node:
#     def __init__(self, val, n):
#         self.value = val
#         self.next = n
        
# class Stack:
#     head = None
#     pointer = -1
    
#     def push(self, value):
#         if self.head == None:
#             self.head = Node(value, None)
#             self.pointer += 1
#         else:
#             n = Node(value, None)
#             n.next = self.head
#             self.head = n
#             self.pointer += 1 
            
#     def peek(self):
#         if self.head == None:
#             return None
#         return (self.head.value)
    
#     def pop(self):
#         if self.head == None:
#             return None
#         temp = self.head
#         self.head = self.head.next
#         temp.next = None
#         self.pointer -= 1
#         return temp.value
   
        
# def checkBrackets(string):
#     stk = Stack()
#     counter_stk = Stack()
#     leftBrackets = ["(", "{", "["]
#     rightBrackets = [")", "}", "]"]
#     count = 1
#     for i in string:
#         if i in leftBrackets:
#             stk.push(i)
#             counter_stk.push(count)
#         if i in rightBrackets:
#             if stk.pointer == -1:
#                 print("Unbalanced")
#                 return
#             else:
#                 validity = False
#                 n = stk.pop()
#                 c = counter_stk.pop()
#                 if n == "(" and i == ")":
#                     validity  = True
#                 elif n == "{" and i == "}":
#                     validity = True
#                 elif n == "[" and i == "]":
#                     validity = True
#                 else:
#                     validity = False
                    
#                 if validity != True:
#                     print("Unbalanced")
#                     return
#         count += 1   
        
#     if stk.pointer == -1:
#         print("Balanced")
#         return
#     else:
#         print("Unbalanced")
    
# a = input("give a string: ")
# checkBrackets(a)





# ###################################################################
# ###################  Task 2 #################################
# ############################################################ Task 2  #############################################
# ##### Using linked list based stack
class Node:
    def __init__(self, val, n):
        self.value = val
        self.next = n
        
class Stack:
    head = None
    pointer = -1
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.pointer += 1
        else:
            n = Node(value, None)
            n.next = self.head
            self.head = n
            self.pointer += 1 
            
    def peek(self):
        if self.head == None:
            return None
        return (self.head.value)
    
    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.pointer -= 1
        return temp.value
   
        
def checkBrackets(string):
    stk = Stack()
    counter_stk = Stack()
    leftBrackets = ["<"]
    rightBrackets = [">"]
    count = 1
    x=0
    for i in string:
        if i in leftBrackets:
            stk.push(i)
            counter_stk.push(count)
        if i in rightBrackets:
            if stk.pointer == -1:
                #print(x)
                #return
                pass
            else:
                validity = False
                n = stk.pop()
                c = counter_stk.pop()
                if n == "<" and i == ">":
                    validity  = True
                    x+=1
                else:
                    validity = False
                    
                if validity != True:
                    print(x)
                    return
        count += 1   
        
    if stk.pointer == -1:
        print(x)
        return
    else:
        print(x)
    

checkBrackets(input("give string: "))