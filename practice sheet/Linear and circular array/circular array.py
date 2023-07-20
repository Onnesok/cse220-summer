#########  1  #################

# def greater_num(n, arr):
#     ar1 = [0]*n
#     cnt = 0

#     for i in range(n):
#         idx = i
#         for j in range(i, i+n, 1):
#             if arr[i] < arr[idx]:
#                 ar1[cnt] = arr[idx]
#                 cnt+=1
#                 break
#             idx = (idx+1)%n

#         if arr[i] >= arr[(idx)%n]:
#             ar1[cnt] = -1
#             cnt+= 1
        
#     print(ar1)

# greater_num(5, [1,2,5,5,4])


##########  2   ######################

# def ninja(n, arr):
#     ar1 = [0]*n
#     cnt = 0
#     st = 0
#     idx = 0
#     for i in range(n):
#         idx = i
#         for j in range(i, i+n, 1):
#             if arr[i] < arr[idx]:
#                 ar1[cnt] = arr[idx]
#                 cnt+=1
#                 break
#             idx = (idx+1)%n

#         if arr[i] >= arr[(idx)%n]:
#             ar1[cnt] = -1
#             cnt+= 1
        
#     print(ar1)

# ninja(5, [1,6,4,3,5])

###########  3  #################

def maximum(arr):
    idx = 0
    s = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
    for i in range(len(arr)):
        print(abs(arr[i] - arr[(idx+1)%len(arr)]), end=" ")
        print()
        s += abs(arr[i] - arr[(idx+1)%len(arr)])
        idx = (idx+1)%len(arr)
        
    print(arr,s)

# maximum([4,2,1,8])


###########  4  ################

# def optimum(n, arr):
#     flag = 99999999999
#     for i in range(n):
#         temp = abs(arr[(i+1)%n] - arr[i])
#         if temp < flag:
#             flag = temp
    
#     print(flag)

# optimum(5, [10,20,30,40, 42])

############  5  #############

######  hurrr bad de  #######

pass

############ 6  ############

####hurr #

pass

##########  7   ##########

#hurrrr

pass
