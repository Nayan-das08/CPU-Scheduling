def showMat(arr):
    for i in range(len(arr)):
        print(arr[i])

n = int(input("Enter no. of processes : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()
    
m = int(input("Enter no. of resource types : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()
max = []
need = []#[[0]*m]*n
allocation = []
work = []
available = []
total = []

# to be enetered by user
print()
for i in range(m):
    print(f"Enter instances of R{i} : ", end='')
    x = int(input())
    total.append(x)

# to be enetered by user
allocation = [
    [0,0,1,2],
    [2,0,0,0],
    [0,0,3,4],
    [2,3,5,4],
    [0,3,3,2],
]

# to be enetered by user
max = [
    [0,0,1,2],
    [2,7,5,0],
    [6,6,5,6],
    [4,3,5,4],
    [0,6,5,2]
]

# fill need[][]
for i in range(len(allocation)):
    x = []
    for j in range(m):
        x.append(max[i][j] - allocation[i][j])
    need.append(x)    

print('\nallocation')
showMat(allocation)

print('\n\nmax')
showMat(max)

print('\n\nneed')
showMat(need)

for j in range(m):
    sum = 0
    for i in range(n):
        sum = sum + allocation[i][j]
    available.append(total[j] - sum)

print()
print(f'total       = {total}')
print(f"available   = {available}")

# SAFETY ALGORITHM
work = available[:]
finish = [False]*n
temp = need[:]

print()


for i in range(n):
#i = 0
    if (finish[i] == False):    
        flag = 1
        for j in range(m):
            if need[i][j] > work[j]:
                flag = 0
                print(i,j)
                #break        
        
        if flag == 1:   # found P[i] where finish[i] is false and need[i] < work
            print(f'P{i}', end='')
            for j in range(m):
                work[j] = work[j] + allocation[i][j]
            finish[i] = True
            print(f'\t{work}')

5
4
6
7
12
12
