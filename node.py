##################################  Task 1  ###########################
class keyidx:
    def __init__(self, arr):
        self.arr = arr
                
    def search(self, val):
        mx = 0
        mn = 0
        for i in range(len(self.arr)):
            if self.arr[i] > mx:
                mx = self.arr[i]
            elif self.arr[i] < mn:
                mn = self.arr[i]
                posmn = abs(mn)
        aux = [0] * (mx + abs(mn) + 1)
        for i in range(len(self.arr)):
            c = self.arr[i]
            if c < 0:
                aux[c+posmn] += 1
            else:
                aux[c+posmn] += 1
                
        for i in range(len(aux)):
            if val+posmn <= len(aux) and val+posmn <= mx+posmn and val+posmn >= 0:
                if aux[val + posmn] >= 1 and val+posmn >= 0:
                    return True
                else:
                    return False
            else:
                return False
            
    def sort(self):
        mx = 0
        mn = 0
        for i in range(len(self.arr)):
            if self.arr[i] > mx:
                mx = self.arr[i]
            elif self.arr[i] < mn:
                mn = self.arr[i]
                posmn = abs(mn)
            aux = [0] * (mx + abs(mn) + 1)
        for i in range(len(self.arr)):
            c = self.arr[i]
            if c < 0:
                aux[c+posmn] += 1
            else:
                aux[c+posmn] += 1
                
        for i in range(len(aux)):
            for j in range(aux[i]):
                print(i - posmn, end=" ")

x = [5, 7, -7, -5, -6, -3, -3]         
a = keyidx(x)
print(a.search(-7))
print(a.search(7))
print(a.search(-70))
a.sort()

###############################  Task 2  ##############################

def hash(strr):
    count = 0
    summ = 0
    for i in range(len(strr)):
        if strr[i] != 'A' and strr[i] != 'E' and strr[i] != 'I' and strr[i] != 'O' and strr[i] != 'U' and (not (strr[i] >= '0' and strr[i] <= '9')):
            count += 1
        elif (strr[i] >= '0' and strr[i] <= '9'):
            summ = summ + int(strr[i])
    return (count * 24 + summ)%9



string = []
hash_table = ["-1"]*9

for i in range(9):
    data = str(input("enter input: "))
    string.append(data)
val = 0
i = 0
nxt = 0
size = 0

while size < 9:
    val = (hash(string[i])+nxt)%9
    if(hash_table[val] == "-1"):
        hash_table[val] = string[i]
        i+=1
        size+=1
        nxt=0
    else:
        nxt=nxt+1
        
#display the hash table
print ("HASH TABLE")
print ("INDEX-ELEMENT")
for i in range (9):
    print (str(i)+"\t"+hash_table[i])
    

# keyindex and hash