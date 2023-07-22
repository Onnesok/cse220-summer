##########  1st  ##################
########  list based   ############

class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem
        self.next = next
        
        
class stack:
    head = None
    pointer = -1
    def __init__(self) -> None:
        self.head = None
    
    def push(self, elem):
        if self.head == None:
            self.head = Node(elem, None)
            self.pointer += 1
        else:
            node = Node(elem, None)
            node.next = self.head
            self.head = node
            self.pointer += 1
    def peek(self):
        if self.pointer == -1:
            print("no element left")
            return None
        else:
            print(self.head.elem)
            
    def pop(self):
        if self.pointer == -1:
            print("no element to pop")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.pointer -= 1
            return temp.elem
            
            
# def check(string):
#     stk = stack()
#     counter_stk = stack()
#     count = 1
#     left_brackets = ["(", "{", "["]
#     right_brackets = [")", "}", "]"]
#     for i in range(len(string)):
#         if string[i] in left_brackets:
#             stk.push(string[i])
#             counter_stk.push(count)
#         elif string[i] in right_brackets:
#             if stk.pointer == -1:
#                 print("unbalanced")
#                 return False
#             else:
#                 validity = False
#                 n = stk.pop()
#                 c = counter_stk.pop()
#                 if n == "(" and string[i] == ")":
#                     validity = True
#                 elif n == "{" and string[i] == "}":
#                     validity = True
#                 elif n == "[" and string[i] == "]":
#                     validity = True
#                 else:
#                     validity = False
                
#                 if validity == True:
#                     pass
#                 else:
#                     print("unbalanced")
#                     return False 
                
#         count+=1
        
#     if stk.pointer == -1:
#         print("balanced")
#         return 
#     else:
#         print("unbalanced")


# string = input("please enter a string of brackets: ")
# check(string)



# ######################  1nd   ####################



# class Node:
#     def __init__(self, elem = None, next = None):
#         self.elem = elem
#         self.next = next
        
        
# class stack:
#     head = None
#     pointer = -1
#     def __init__(self) -> None:
#         self.head = None
    
#     def push(self, elem):
#         if self.head == None:
#             self.head = Node(elem, None)
#             self.pointer += 1
#         else:
#             node = Node(elem, None)
#             node.next = self.head
#             self.head = node
#             self.pointer += 1
#     def peek(self):
#         if self.pointer == -1:
#             print("no element left")
#             return None
#         else:
#             print(self.head.elem)
            
#     def pop(self):
#         if self.pointer == -1:
#             print("no element to pop")
#             return None
#         else:
#             temp = self.head
#             self.head = self.head.next
#             self.pointer -= 1
#             return temp.elem
            
            
# def check(string):
#     stk = stack()
#     counter_stk = stack()
#     count = 1
#     left_brackets = ["(", "{", "["]
#     right_brackets = [")", "}", "]"]
#     for i in range(len(string)):
#         if string[i] in left_brackets:
#             stk.push(string[i])
#             counter_stk.push(count)
#         elif string[i] in right_brackets:
#             if stk.pointer == -1:
#                 print("unbalanced")
#                 return False
#             else:
#                 validity = False
#                 n = stk.pop()
#                 c = counter_stk.pop()
#                 if n == "(" and string[i] == ")":
#                     validity = True
#                 elif n == "{" and string[i] == "}":
#                     validity = True
#                 elif n == "[" and string[i] == "]":
#                     validity = True
#                 else:
#                     validity = False
                
#                 if validity == True:
#                     pass
#                 else:
#                     print("unbalanced")
#                     return False 
                
#         count+=1
        
#     if stk.pointer == -1:
#         print("balanced")
#         return 
#     else:
#         print("unbalanced")


# string = input("please enter a string of brackets: ")
# check(string)

#######################  3rd  #####################

# def reverse(a):
#     count = 0
#     stk = stack()
#     for i in range(len(a)):
#         stk.push(a[i])
#         count+= 1
    
#     for i in range(count):
#         print(stk.pop(), end = "")


# a = "cse220"
# reverse(a)

###################  4th  ###############

# def palindrome(a):
#     l = len(a)//2
#     stk = stack()
#     validity = True
    
#     for i in range(l):
#         stk.push(a[i])
#     if len(a)%2 == 0:
#         for i in range(l, len(a), 1):
#             x = stk.pop()
#             if a[i] != x:
#                 validity = False
#                 break
#     elif len(a) % 2 != 0:
#         for i in range(l+1, len(a), 1):
#             x = stk.pop()
#             if a[i] != x:
#                 validity = False
#                 break    
#     print(validity)


# a = "madam"
# palindrome(a)

# a = "cse220"
# palindrome(a)


#############  5th  ##############
## pop kore push korle line er last ei jaitese
# ar sandwith just pop kore dilei ok
# do this untill pointer = -1
# if pointer = -1 now count stack of students
# those students the the output or answer  simple but boro
pass

################  6th  #################

# khatay


##########  7th  ############

# khatay