n = int(input("Enter no. of processes : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()
    
m = int(input("Enter no. of resource types : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()
max = [[0]*m]*n
need = [[0]*m]*n
allocation = [[0]*m]*n
work = []
available = []
total = []

print()
for i in range(m):
    print(f"Enter instances of R{i} : ", end='')
    x = int(input())
    total.append(x)


allocation = [
    [0,0,1,2],
    [2,0,0,0],
    [0,0,3,4],
    [2,3,5,4],
    [0,3,3,2],
]

max = [
    [0,0,1,2],
    [2,7,5,0],
    [6,6,5,6],
    [4,3,5,4],
    [0,6,5,2]
]

# fill need[][]
for i in range(len(allocation)):
    for j in range(m):
        need[i][j] = max[i][j] - allocation[i][j]

    


for j in range(m):
    sum = 0
    for i in range(n):
        sum = sum + allocation[i][0]
        #print(allocation[i][0])
    print(sum)
    available.append(total[j] - sum)

print(total)
print(available)

'''for i in range(len(allocation)):
    print(allocation[i])

print()
for i in range(len(max)):
    print(max[i])
'''    
    
