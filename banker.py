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

iterations = 0
safe = 0
while (iterations < 10) and (False in finish):
    for i in range(n):
    #i = 0
        if (finish[i] == False):    
            flag = 1
            for j in range(m):
                if need[i][j] > work[j]:
                    flag = 0
                    print(f"ignored : {i,j}")
                    #break        
            
            if flag == 1:   # found P[i] where finish[i] is false and need[i] < work
                print(f'P{i}', end='')
                for j in range(m):
                    work[j] = work[j] + allocation[i][j]
                finish[i] = True
                print(f'\t{work}')
    
    print(f"after {iterations+1} iterations",end='')
    if False in finish:
        print("\tFalse in finish[]")
    else:
        print("\tAll True in finish[]")
        safe = 1
    iterations += 1

if safe == 1:
    print("\n\nThe system is in SAFE STATE!")

#------------------------------------------------------------

print('\n')
request = []
x = int(input("Enter Process ID which is requesting resources : "))

print(f"\nRequesting p{x}")
for i in range(m):
    print(f"\tEnter instances of R{i} : ", end='')
    z = int(input())
    request.append(z)


for i in range(m):
    # step 1
    if request[i] <= need[x][i]:
        # step 2
        if request[i] <= available[i]:
            # step 3
            for j in range(m):
                available[j]  = available[j] - request[j]
                allocation[x][j] = allocation[x][j] + request[j]
                need[x][j] = need[x][j] - request[j]
            # now perform safety algo
        else:
            print(f"P{x} needs to wait as resources are not available")
            exit
    else:
        print("Request is more than needed instances")
        exit

# SAFETY ALGORITHM after Recource-Request Allocation
work = available[:]
finish = [False]*n
temp = need[:]

print()

iterations = 0
safe = 0
while (iterations < 10) and (False in finish):
    for i in range(n):
    #i = 0
        if (finish[i] == False):    
            flag = 1
            for j in range(m):
                if need[i][j] > work[j]:
                    flag = 0
                    print(f"ignored : {i,j}")
                    #break        
            
            if flag == 1:   # found P[i] where finish[i] is false and need[i] < work
                print(f'P{i}', end='')
                for j in range(m):
                    work[j] = work[j] + allocation[i][j]
                finish[i] = True
                print(f'\t{work}')
    
    print(f"after {iterations+1} iterations",end='')
    if False in finish:
        print("\tFalse in finish[]")
    else:
        print("\tAll True in finish[]")
        safe = 1
    iterations += 1

if safe == 1:
    print(f"\n\nThe system is in SAFE STATE!")
    print(f"request {request} CAN be allocated")
else:
    print(f"\n\nThe system is NOT in SAFE STATE!")
    print(f"request {request} CANNOT be allocated")


5
4
6
7
12
12
