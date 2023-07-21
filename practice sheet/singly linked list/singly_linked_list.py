class Node:
    def __init__(self, elem = None, next = None):
        self.elem = elem
        self.next = next
        
        
        
        
# class singly:
#     def __init__(self, arr):
#         self.head = None
#         if type(arr) == list:
#             self.head = Node(arr[0])
#             head = self.head
#             t = head
#             for i in range(1 ,len(arr), 1):
#                 t = Node(arr[i], None)
#                 head.next = t
#                 head = t
                
#         elif type(arr) == Node:
#             self.head = arr
            
            
#     def list_print(self):
#         t = self.head
#         while t != None:
#             print(t.elem)
#             t = t.next
            
#     #####################  Question 1  ################
#     def replace(self):       
#         t = self.head  #  tail
#         head = t   # dummy head
#         new = None  # new dummy list
        
#         last_element = self.head
#         while last_element.next!= None:
#             last_element = last_element.next
        
#         new = Node(last_element.elem, None)  # ok  now list is filled from None
#         node = new
        
#         while t != last_element:
#             h = Node(t.elem, None)
#             node.next = h  
#             node = h       
#             t = t.next          # nothing to do with t ..... just using for iterating
            
#         # ok now printing
#         tail = new
#         while tail != None:
#             print(tail.elem, end = " ")  # done weeeee
#             tail = tail.next
        
            
# s = singly([10,20,30,40,60])
# #s.list_print() 
# s.replace()


##############  Question 2 ###############

#### dummy code cause alsemi lagtese

class habijabi:
    def __init__(self) -> None:
        pass
    def intersect(self, head1, head2):
        t1 = head1
        temp = head2   # jist using for storing data of head2
        t2 = temp       # ops dump
        self.new_node_head = None
        new_node = self.new_node_head
        
        while t1 != None:
            while t2 != None:
                if t1 == t2:
                    if self.new_node_head == None:
                        self.new_node.head = Node(t1.elem, None)
                        new_node = self.new_node_head
                    else:
                        x = Node(t1.elem, None)
                        new_node.next = x
                        new_node = x
                    break
                t2 = t2.next
            t1 = t1.next
            
            # draft code 
            
            
            
###############  Question 3  ####################

pass

###############  Question 4  ##################

### iterate korbo

## even er jonne ekta list korbo....
# odd er jonne ekta list korbo

# last e list1 er tail er sathe list 2 er head + kore dibo


# assignment e korsilam..............


###############   Question 5  #################


# first e count korbi
# then count - n korbi, so first theke koto tomo position pabi
# next oi position pporjonto iterate kore last er t return

# done

############# Question 6  ###############

# itearate koira count kor
# next if count%2 == 0(even) naki odd ber kor
# odd hoile count/2 porjonto iterate koira return value
# else (count/2)+1 porjonto iterate kore return value


##############  Question 7  ###############

#  https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/ 
#  :`)
pass

###############  Question 8  #################

## ok habijabi jinis eida....... pore korbo....easy ase

#############  Question 9 ################

# ok so my approach is count this list
# iterate to floor devision or half of the list
# now create a new list in reversed with rest of the list
# now if 1st list == new list then palindrome.   else nope mara kha


##########  Question 10  ###############

# just remove even nodes


##########  11   ###########

# just compare
#example

# while t!= None:
#     cnt = 0
#     while t1 != None:
#         if t != t1:
#             cnt+=1
#             break
#         t1 = t1.next
#         if t == t1:
#             break
#     if cnt > 0:
#         break

#     t = t.next
    
# if cnt == 0:
#     print("identical")
# else:
#     print("not identical")


###########  12  ##################

# len - k hosse second idx jetar sathe k swap hobe
# now do the swap and return head... simple