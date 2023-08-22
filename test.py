import numpy as np

def r(arr):
    rs = -9999
    
    for i in range(len(arr)):
        temp = 99999
        for j in range(len(arr[i])):
            if arr[i][j] < temp:
                temp = arr[i][j]
            
        if temp > rs:
            rs = temp
    return rs


print(r([[2,7,5],[9,3,8],[1,4,6]]))
print(r([[2,7,5,10], [9,13,8,4]]))