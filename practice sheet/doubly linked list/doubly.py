##############  1  #################
class Node:
    def __init__(self, elem = None, next = None, prev = None):
        self.elem = elem
        self.next = next
        self.prev = prev
        
class doubly1:
    def __init__(self, a):
        self.head = None
        node =  None
        self.tail = None
        
        if type(a) == Node:
            self.head = a
        
        elif type(a) == list:
            for i in range(len(a)):
                new_node = Node(a[i], None, None)
                
                if self.head == None:
                    self.head = new_node
                    node = new_node
                else:
                    node.next = new_node
                    new_node.prev = node
                    node = node.next
                    
        self.tail = node
    
    ################  Question 1 #####################    
    def palindrome(self):
        t = self.head
        cnt = 0
        while t!= None:
            cnt+=1
            t = t.next
            
        
        t = self.head
        rev = self.tail
        k = cnt//2
        flag = 0
        pal = True
        while flag!= k:
            if t.elem == rev.elem:
                print(t.elem)
                flag += 1
            elif t.elem != rev.elem:
                pal = False
                break
            rev = rev.prev
            t=t.next
        if pal == True:
            print("palindrome")
        elif pal == False:
            print("not palindrome")
            
    #############  Question 2  ############
    # just value jodi bujhay taile just reverse print
            

################# question 3 ##############            
    def largest(self):
        head = self.head
        tail = self.tail
        head.prev = tail
        tail.next = head
        node = head.next
        large = head.elem
        
        while node != head:
            if node.elem > large:
                large = node.elem
            node = node.next
        print(large)
    
    ############  Question 4  #############
    def left(self):
        head = self.head
        tail = self.tail
        head.prev = tail
        tail.next = head
        node = head
        k = 1
        flag = 0
        while flag != k:
            node = node.next
            flag += 1
        head = node
        print(head.elem)

    ###################  Question 5  #############
    def right(self):
        head = self.head
        tail = self.tail
        head.prev = tail
        tail.next = head
        node = head
        k = 1
        flag = 0
        while flag != k:
            node = node.prev
            flag += 1
        head = node
        
        
        # lets validate
        # # jehetu t.next e mane next value te chole  jassi tai first element bad portese
        print(head.elem)  # ejonne print first element
        t = head.next
        while  t != head:
            print(t.elem)
            t = t.next

    

a = doubly1([1,7,7,1,12,50])
#a.palindrome()
#a.largest()
# a.left()
a.right()
