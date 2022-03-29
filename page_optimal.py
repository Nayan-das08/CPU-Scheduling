'''ref = []
m = int(input("Enter number of characters in ref. string : "))
for i in range(m):
    print(f"  ref[{i}] : ", end='')
    x = int(input())
    ref.append(x)
'''

ref = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

print("ref.string \tframes \t\tstack")
#n = int(input("\nEnter number of free frames : "))
n = 3
frames = [0]*n
stack = []
j = 0
count = 0 

for i in range(len(ref)):
    print(f"     {ref[i]}\t", end='')
    
        