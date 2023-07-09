import numpy as np
def arrangement(m, diff):
  cnt = 0
  j=1
  for i in range(len(m)):  #4 row
    for j in range(len(m[0])):
        if abs(m[i][j] - m[j][i]) == diff:
            pass
    else:
      cnt+= 1
    print(i, j)
  if cnt> 0:
    tf = False
  else:
    tf = True
  return tf 

m = np.array([[7,13,9,14],[12,8,15,11],[10,17,3,2],[15,10,1,4]])
print_matrix(m)
print()
returned_value = arrangement(m,1)
print(returned_value)#This should print False
unittest.output_test(returned_value, False)

m = np.array([[8,15,7,12],[13,2,18,11],[9,20,5,2],[14,9,0,10]])
print_matrix(m)
print()
returned_value = arrangement(m,2)
print(returned_value)#This should print True
unittest.output_test(returned_value, True)