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
        return 

print(pi("xpix"))