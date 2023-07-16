# ########### 1st #############

# def union(n, m, a, b):
#     cnt = 0
#     arr = [0]*n*m
#     for i in range(n):
#         if a[i] in arr:
#             pass
#         else:
#             arr[cnt]  = a[i]
#             cnt += 1
#     for j in range(m):
#         if b[j] in arr:
#             pass
#         else:
#             arr[cnt] = b[j]
#             cnt += 1
    
#     print(cnt)
    
    
# union(5,4,[1,2,3,4,5], [1,2,3,7])  # answer : 1 2 3 4 5 7  (does the union thing)

#######  2nd #########

# def sorting(n, arr):
#     cnt = 0
#     ar1 = [0]*n
#     for i in range(n):
#         if arr[i] >= 0:
#             ar1[cnt] = arr[i]
#             cnt+=1
#     for i in range(n):
#         if arr[i] < 0:
#             ar1[cnt] = arr[i]
#             cnt+=1
#     print(ar1)

# sorting(8, [1, -1, 3, 2, -7, -5, 11, 6])

######  3rd ################

# def subarray(n, s, arr):
#     a1 = 0
#     a2 = 0
#     rs = 0
#     for i in range(n):
#         sum = 0
#         a1 = i + 1 
#         for j in range(i,n,1):
#             sum = sum + arr[j]
#             if sum >= s:
#                 break
#         if sum == s:
#             a2 = j + 1
#             break
#     print(a1, a2)

# subarray(10,15,[1,2,3,4,5,6,7,8,9,10])

######  4th  ###########

# def freq(n, arr, x):
#     cnt = 0
#     for i in range(n):
#         if arr[i] == x:
#             cnt+= 1
#     print(cnt)

# freq(5, [1,2,3,1,1], 1)

#### 5th #####

# def kthelem(n, arr, k):
#     cnt = 0
#     elem = -1
#     a1 = [-1] * n
#     for i in range(n):
#         for j in range(n-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#     for i in range(k):
#         pass
#     elem = arr[i]
#     print(elem)
    
# kthelem(5, [7, 10, 4, 20, 15], 4)

#passing


##### 6th ######
    
# def array_sort(n, arr):
#     for i in range(n):
#         for j in range(n-1):
#             if arr[j] > arr[j+1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#     print(arr)

# array_sort(5, [0,2,1,2,0])


###########   7th #############

# def block(n, arr):
#     sum = 0
#     for i in range(1, n-1, 1):
#         if arr[0] >= arr[n-1]:
#             sum = sum + (int(arr[n-1]) - int(arr[i]))
#         else:
#             sum = sum + (int(arr[0] - int(arr[i])))
#         if sum <= 0:
#             sum = 0
#     print(sum)

# block(4, [7,4,0,9])

#########  8th  #############

# def wave(n, arr):
#     for i in range(0, n-1, 2):
#         temp = arr[i]
#         arr[i] =  arr[i+1]
#         arr[i+1] = temp
#     print(arr)

# wave(6, [2,4,7,8,9,10])

##########  9th  ############

# def majority(n, a):
#     temp = n/2
#     cnt = 0
#     majority = [-1]*n
#     for i in range(n):
#         c = 0
#         elem = 0
#         for j in range(i, n, 1):
#             if a[i] == a[j]:
#                 elem = a[i]
#                 c+=1
#         if c > temp:
#             majority[cnt] = elem
#             cnt+=1
            
#     if cnt > 0:
#         for i in range(cnt):
#             print(majority[cnt-1], end=' ')
#     else:
#         print(-1)
        
# majority(3, [1,2,3])

######  10   ########

# def jump(n, arr):
#     cnt = 0
#     i=0
#     while i < n:
#         if arr[i] == 0:
#             print(-1)
#             break
#         if i < n:
#             i = i + arr[i]
#             cnt+=1
#         if i+1 >= n:
#             break
#     print(cnt)

# jump(6, [1,4,3,2,6,7])
# jump(11, [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])

##### 11 #######

# def tower(k, n, arr):
#     min = 999999
#     max = -9999999
#     for i in range(n):
#         if arr[i] - k <= 0:
#             arr[i] = arr[i] + k
#         else:
#             arr[i] = arr[i] - k
    
#     for i in range(n):
#         if min > arr[i]:
#             min = arr[i]
#         if max < arr[i]:
#             max = arr[i]
#     rs = max-min
#     print(arr, rs)

# tower(2,4,[1,5,8,10])
# tower(3,5,[3,9,12,16,20])

###### 12 #######

