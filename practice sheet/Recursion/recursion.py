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
    else:
        if n[0] == "p" and n[1] == "i":
            return "3.14" + pi(n[2:])
        else:
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
    pass

print(count("abcxxabc"))