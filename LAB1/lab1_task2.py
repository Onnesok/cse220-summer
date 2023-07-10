import math

def minfunction(arr):
  sum = 0
  cnt = 0
  for i in range(len(arr)):

    sum = sum + arr[i]
    cnt+= 1 
  return sum/cnt


def std(arr, mean):
  t1 = 0
  n=len(arr)-1
  for i in arr:
    t1 = t1+ (i- mean)**2
  total = math.sqrt((t1/n))
  return total

def newarr(arr, mean, std):
  cnt = 0
  for i in range(len(arr)):
    x = mean + (1.5*float(std))
    if arr[i] >= x:
      cnt+=1
    else:
      x = mean-(1.5*float(std))
      if arr[i] <= x:
        cnt+=1
    newar = [0]*cnt
    
    
    idx = 0
  for i in range(len(arr)):
    x = mean + (1.5*float(std))
    if arr[i] >= x:
      newar[idx] = arr[i]
      idx+=1
    else:
      x = mean-(1.5*float(std))
      if arr[i] <= x:
        newar[idx] = arr[i]
        idx+=1
  return newar

##########################  function call #########################
arr = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
mean = minfunction(arr)
print("The mean number is:", mean)


std = "{:.2f}".format(std(arr, mean))
print("The standard daviation is:", std)

new = newarr(arr, mean, std)
print("New array:",new)