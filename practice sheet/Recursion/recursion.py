############## 1 ################
def sumdigits(n):
    if n < 1:
        return 0
    else:
        return n % 10 + sumdigits(n//10)

# a = sumdigits(126)
# print(a)


############## 2  #################
def bunny(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return 3 + bunny(n-1)
        else:
            return 2 + bunny(n-1)

# print(bunny(2))

################### 3 ##############

def occurances7(n):
    if n == 0:
        return 0
    else:
        if n % 10 == 7:
            return 1 + occurances7(n//10)
        else:
            return 0 + occurances7(n//10)

# print(occurances7(7177))

####################  4  ###################

def lowerr(n):
    x = len(n)
    if x == 0:
        return 0
    else:
        if n[x-1] == 'x':
            return 1 + lowerr(n[:-1])
        else:
            return 0 + lowerr(n[:-1])

# print(lowerr("xhixhix"))

#################  5  ################

def pi(n):
    if len(n) == 0:
        return ""
    elif len(n) >= 2:
        if n[0] == "p" and n[1] == "i":
            return "3.14" + pi(n[2:])
        else:
            return n[0] + pi(n[1:])
    return n[0] + pi(n[1:])

#print(pi("xpipix"))

############### 6  #################

def arr11(arr, idx = 0):
    if len(arr) == idx:
        return 0
    else:
        if arr[idx] == 11:
            return 1 + arr11(arr, idx = idx+1)
        else:
            return 0 + arr11(arr, idx = idx+1)

# print(arr11([1,2,11,0,11], 0))

################  7  ################

def pairstar(n):
    if len(n) == 1:
        return n[0]
    else:
        if n[0] == n[1]:
            return n[0] + "*" + pairstar(n[1:])
        else:
            return n[0] + pairstar(n[1:])

#print(pairstar("hellooooapp"))

###############  8  #############

def count(n):
    if len(n) < 3:
        return 0
    else:
        if len(n) >= 3:
            if n[0] == 'a' and n[1] == 'b' and (n[2] == 'c' or n[2] == 'a'):
                return 1 + count(n[1:])
            else:
                return count(n[1:])

#print(count("abcxxaba"))


#############  9  ###############

def count_hi(n):
    if len(n) < 2:
        return 0
    else:
        if len(n) >= 2:
            if n[:2] == 'hi':
                if len(n) >= 3:
                    if n[2] == 'x':
                        return count_hi(n[1:])
                    
                return 1 + count_hi(n[1:])
            return count_hi(n[1:])

#print(count_hi('axhixhihi'))


##############  10  #############

def sub_str(n, sub):
    if len(n) < len(sub):
        return 0
    else:
        if n[:len(sub)] == sub:
            return 1 + sub_str(n[1:], sub)
        return sub_str(n[1:], sub)


#print(sub_str('catcowcat', 'cow'))

#################  11 ###############

def bunny(n):
    if n == 0:
        return 0
    else:
        return 2 + bunny(n-1)

#print((bunny(3)))

###########  12  ##############

def triangle(n):
    if n == 0:
        return 0
    else:
        return triangle(n-1) + n

#print(triangle(2))

##########  13  ##########

def noX(n):
    if len(n) == 0:
        return ""
    else:
        if n[0] != "x":
            return n[0] + noX(n[1:])
        return noX(n[1:])

#print(noX("xbcaxb"))

##########  14  ##########

# def array220(n, idx):
#     if len(n) == idx:
#         return False
#     else:
#         if idx+1 <= len(n)-1 and n[idx]*10 == n[idx+1]:
#             return True
#         return array220(n, idx+1)

#print(array220([3,3,2,20], 0))

#######@@@@@@@@@@ not sure though

############# 15  #########

def endX(n):
    if len(n) == 0:
        return ""
    else:
        if n[0] != 'x':
            return n[0] + endX(n[1:])
        else:
            return endX(n[1:]) + 'x'

#print(endX('xxhisxx'))

########## 16  ###########

def count11(n):
    if len(n) == 0:
        return 0
    else:
        if n[:2] == '11':
            return 1 + count11(n[2:])
        return count11(n[1:])

#print(count11("11abc11"))

###########  17  ##########

def paren_bit(n):
    if n[0] == ")":
        return ""
    else:
        if n[0] == "(" and n[-1] == ")":
            return n
        if n[0] == "(":
            return paren_bit(n[:-1])
        return paren_bit(n[1:])

#print(paren_bit("yo(abcd)123"))

###########  18  ##############

def str_copy(arr, cp, times):
    if len(cp) * times > len(arr):
        return False
    elif arr[:len(cp)] == cp:
        if times == 1:
            return True
        else:
            return str_copy(arr[1:], cp, times-1)
    else:
        return str_copy(arr[1:], cp, times)
        

# x= 'cbxaaat'
# a = 'ab'
# print(x[:len(a)])
# print(x)

#print(str_copy("catcowcat", "cat", 2))

#################  19  #############

def change_x(arr):
    if len(arr) == 0:
        return ""
    else:
        if arr[0] == 'x':
            return 'y' + change_x(arr[1:])
        else:
            return arr[0] + change_x(arr[1:])

#print(change_x('xxhixx'))

######### 20  ##########

def array_6(arr, idx):
    if len(arr) == idx:
        return False
    else:
        if arr[idx] == 6:
            return True
        else:
            return array_6(arr, idx+1)

#print(array_6([1,5,4,3,6], 0))

###############  21  ##########

def all_star(n):
    if len(n) == 0:
        return ""
    else:
        if len(n) == 1:
            return n[0] + all_star(n[1:])
        return n[0] + "*" + all_star(n[1:])

#print(all_star('hello'))


###########  22   ############

def count_pairs(n):
    if len(n) < 3:
        return 0
    else:
        if n[0] == n[2]:
            return 1 + count_pairs(n[1:])
        else:
            return count_pairs(n[1:])

# print(count_pairs('axaxax'))


########  23  ###########

def clean(n):
    if len(n)-1 == 0:
        return ""
    else:
        if n[0] == n[1]:
            return clean(n[1:])
        else:
            return n[0] + clean(n[1:])

# print(clean('abbbbccddddd'))


############  24  ##########

def nest(n):
    if len(n) == 1:
        return False
    else:
        if len(n) == 0:
            return True
        else:
            if n[0] == '(' and n[-1] == ')':
                return nest(n[1:len(n)-1])
            else:
                return False

#print(nest('(((x)))'))


###########  25  ###########

def str_dis(n, sub):
    if len(n) < len(sub):
        return 0
    elif n[:len(sub)] == sub and n[-len(sub):] == sub:
        return len(n)
    elif n[:len(sub)] != sub:
        return str_dis(n[1:], sub)
    elif n[-len(sub):] != sub:
        return str_dis(n[:-1], sub)


#print(str_dis('cccatcowcatxx', 'cat'))

##########  26  ############
    pass
