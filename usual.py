# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)

# #print(fact(5))

# def fibo(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# #print(fibo(5))

# def pr(n):
#     if len(n) == 0:
#         return
#     else:
#         pr(n[1:])
#         print(n[0])

# #pr([10,20,30,40,50])


# def bi(n):
#     rem = n%2
#     if n == 0:
#         return ""
#     else:
#         return bi(n//2)+str(rem)
#         print(rem)

# #print(bi(12))

# ###########################
# ###########################
# ############################
# ###########################
# ###########################
# ############################
# ###########################
# ###########################
# ############################       2BBB
# ###########################
# ###########################
# ############################
# ###########################
# ###########################
# ############################

# def flatten(n, a):
#     if len(n) == 0:
#         return a
#     else:
#         if type(n[0]) == int:
#             a.append(n[0])
#             return flatten(n[1:], a)
#         else:
#             a = flatten(n[0], a)
#             return flatten(n[1:], a)



# # given_list = [1, 2,[16,8], [3,4]]
# # #given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
# # output = flatten(given_list, [])
# # print(output)

# def summ(n):
    
#     if n == 0:
#         return 0 
#     else:
#         return n%10 + summ(n//10)
    
# #print(summ(126))

# def cnt7(n):
#     if n == 0:
#         return 0
#     else:
#         if n%10 == 7:
#             return 1 + cnt7(n//10)
#         return 0 + cnt7(n//10)

# #print(cnt7(7177))

# def pii(n):
#     if len(n) == 0:
#         return ""
#     else:
#         if n[:2] == "pi" and len(n) >= 2:
#             return "3.18" + pii(n[2:])
#         else:
#             return "x" + pii(n[1:])

# # print(pii('xpixpipi'))


# def c11(n):
#     if len(n) == 0:
#         return 0
#     else:
#         if len(n) >= 2:
#             if n[:2] == '11':
#                 return 1 + c11(n[2:])
#             else:
#                 return c11(n[1:])
#         else:
#             return c11(n[1:])

# #print(c11("abc111"))

# def paren_bit(n):
#     if n[0] == ")":
#         return ""
#     else:
#         if n[0] == "(" and n[-1] == ")":
#             return n
#         if n[0] == "(":
#             return paren_bit(n[:-1])
#         return paren_bit(n[1:])

# #print(paren_bit("yo(abcd)123"))

# # import math

# # class sum:
# #     tsum = None

# # class Node:
# #     def __init__(self, elem = None):
# #         self.elem = elem
# #         self.next = None
# #     ##################################
# # def push(head, elem):
# #     if head == None:
# #         new_node = Node(elem)
# #         head = new_node
# #         return head
    
# #     new_node = Node(elem)
# #     new_node.next = head
# #     head = new_node
# #     return head
    
# # def sumnode(head, s):
# #     if head == None:
# #         return
    
# #     else:
# #         sumnode(head.next, s)
# #         s.tsum += head.elem
        
# # def snode(head):
# #     s = sum()
# #     s.tsum = 0
# #     sumnode(head, s)
# #     return s.tsum    

# # head = None

# # head = push(head, 1)
# # head = push(head, 2)
# # head = push(head, 5)
# # head = push(head, 10)

# # print("sum of nodes = ",snode(head))


# def num(i, n):
#   if i == n+1:
#     print()
#     return
#   print(i, end=" ")
#   i = i+1
#   return num(i, n)

# def pattern(a, i):
#   if i == a+1:
#     return
#   num(1, i)
#   pattern(a, i+1)

# #F call
# pattern(5, 1)


# def nss(n, t):
#     if t == n+1:
#         print()
#         return
#     else:
#         print(t, end = " ")
#         t+=1
#         return nss(n, t)

# def pt(n,t):
#     if t == n+1:
#         return
#     else:
#         nss(t, 1)
#         pt(n, t+1)
    

# pt(5, 1)


class BTNode:
    def __init__(self, elem = None, left = None, right = None) -> None:
        self.elem = elem
        self.right = right
        self.left = left
        
        
def tree_construction(arr, i = 1):
    if i >= len(arr) or arr[i] == None:
        return None
    leaf = BTNode(arr[i])
    leaf.left = tree_construction(arr, 2*i)
    leaf.right = tree_construction(arr, 2*i+1)
    return leaf

def inorder(root):
    if root == None:
        return None
    inorder(root.left)
    print(root.elem, end = " ")
    inorder(root.right)
    
def preorder(root):
    if root == None:
        return None
    print(root.elem, end=" ")
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if root == None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.elem, end = " ")



def insertLevelOrder(arr, i, n):
	root = None
	# Base case for recursion
	if i < n:
		root = BTNode(arr[i])

		# insert left child
		root.left = insertLevelOrder(arr, 2 * i + 1, n)

		# insert right child
		root.right = insertLevelOrder(arr, 2 * i + 2, n)
		
	return root


arr = [1, 2, 7, -2, -1, -5, 6]
n = len(arr)
root = None
root = insertLevelOrder(arr, 0, n)
preorder(root)
print()

root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)
print()
preorder(root2)0
print()
postorder(root2)
print()

