# You must run this cell to install dependency
import fhm_unittest as unittest
import numpy as np




# Complete the functions defined in this cell


# Test 01: Play Right
def playRight(sequence,beats):
  for i in range(len(beats)):
    if beats[i] == 1:
      temp = sequence[len(sequence)-1]
      for i in range(len(sequence)-1, 0, -1):
        sequence[i] = sequence[i-1]
      sequence[0] = temp
  
  return sequence


# Test 02: Discard Cards
def discardCards(cards,number):
  for k in range(len(cards)):
      for i in range(len(cards)):
        if cards[i] == number:
          for j in range(i, len(cards)-1):
            cards[j] = cards[j+1]
            cards[j+1] = 0
            
  return cards


#Test 03: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):
  pk1 = np.zeros(len(pokemon_1), dtype=int)
  
  #pk1 = pokemon_1
  for i in range(len(pokemon_1)):
    for j in range(len(pokemon_2)-i-1, -1, -1):
      if pokemon_1[i] == None:
        pokemon_1[i] = 0
      if pokemon_2[j] == None:
        pokemon_2[j] = 0
      pk1[i] = pokemon_1[i] + pokemon_2[j]
      break
  return pk1


# Test 04: Balance your Salami
def balanceSalami(salami):
  cnt = 0
  rs = False
  for i in range(len(salami)):
    cnt += salami[i]
  if cnt%2 == 0:
    rs = True
  else:
    rs = False
  return rs

# Test 05: Protecc Salami
def protectSalami(salami):
  rs = False
  taka = np.zeros(100, dtype=int)
  repeat = np.zeros(100, dtype=int)
  
  for i in range(len(salami)):
    cnt = 0
    if salami[i] not in taka:
      taka[i] = salami[i]
      for j in range(len(salami)):
        if salami[i] == salami[j]:
          cnt += 1
    repeat[i] = cnt
    
  for i in range(len(salami)):
    for j in range(i+1, len(salami)):
      if repeat[i] > 1 and repeat[i] == repeat[j]:
        #print("i",repeat[i])
        #print("j",repeat[j])
        rs = True
        break
  return rs


# Test 05: Odd Even Wave
def waveYourFlag(arr):
  ev = 0
  od = 0
  
  ev1=1
  od1=1
  nar = np.zeros(len(arr), dtype=int)
  #nar = [0]*len(arr)
  for i in range(0, len(arr), 1):
    if arr[0]%2 == 0:
      if arr[i]%2 == 0:
        nar[ev] = arr[i]
        ev+=2
      elif arr[i]%2 != 0:
        nar[od1] = arr[i]
        od1+=2
    
    if arr[0]%2 != 0:
      if arr[i]%2 != 0:
        nar[od] = arr[i]
        od+=2
      elif arr[i]%2 == 0:
        nar[ev1] = arr[i]
        ev1+=2
  return nar






######################################################################
#####################  Driver code  #################################
#####################################################################

# This cell is the driver code
# Run this cell after completion of above function.
# You will see the status Accepted after completion if your code is correct.
# If your function is wrong you will see wrong[correction percentage]
# This is called unit testing if you are wondering the checking approach
# No need to write or change any code here. You can only change the inputs

print("///  Test 01: Play Right  ///")
sequence=np.array([10,20,30,40,50,60])
beats = np.array([1,0,0,1,0,1])
returned_value = playRight(sequence, beats) 
print(f'Task 1: {returned_value}') # This should print [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, np.array([40, 50, 60, 10, 20, 30]))


print("///  Test 02: Discard Cards  ///")
cards = np.array([1,2,3,2,8,2,2,5,7])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1, 3, 8, 5, 7, 0, 0, 0, 0]
unittest.output_test(returned_value, np.array([1, 3, 8, 5, 7, 0, 0, 0, 0]))


print("///  Test 03: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 3: {returned_value}') # This should print [12, 3, 28, -8, 5]
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))

pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 3: {returned_value}') # This should print [4,17,6,27,2]
unittest.output_test(returned_value, np.array([4,17,6,27,2]))

pokemon_1 = np.array([4, 5, None, None])
pokemon_2 = np.array([2, None, None, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 3: {returned_value}') # This should print [4,5,0,2]
unittest.output_test(returned_value, np.array([4,5,0,2]))


print("///  Test 04: Balance Your Salami  ///")
salami = np.array([1, 1, 1, 2, 1])
returned_value = balanceSalami(salami)
print(f'Task 4: {returned_value}') # This should print True
unittest.output_test(returned_value, True)

salami = [2, 1, 1, 2, 1]
returned_value = np.array(balanceSalami(salami))
print(f'Task 4: {returned_value}') # This should print False
unittest.output_test(returned_value, False)

salami = [10, 3, 1, 2, 10] 
returned_value =  np.array(balanceSalami(salami))
print(f'Task 4: {returned_value}') # This should print True
unittest.output_test(returned_value, True)


print("///  Test 05: Protecc Salami  ///")
salami = np.array([4,5,6,6,4,3,6,4]) 
returned_value = protectSalami(salami) 
print(f'Task 5: {returned_value}') # This should print True
unittest.output_test(returned_value, True)

salami = np.array([3,4,6,3,4,7,4,6,8,6,6])
returned_value = protectSalami(salami) 
print(f'Task 5: {returned_value}') # This should print False
unittest.output_test(returned_value, False)


print("///  Test 06: Odd Even Wave  ///")
arr = np.array([2,12,3,8,1,5])
returned_value = waveYourFlag(arr) 
print(f'Task 6: {returned_value}') # This should print [2,3,12,1,8,5]
unittest.output_test(returned_value, np.array([2,3,12,1,8,5]))

arr = np.array([45,23,78,84,41])
returned_value = waveYourFlag(arr) 
print(f'Task 6: {returned_value}') # This should print [45,78,23,84,41]
unittest.output_test(returned_value, np.array([45,78,23,84,41]))