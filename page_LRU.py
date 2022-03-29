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
    
    if ref[i] not in frames:    # page fault

        if len(stack) < 3:
            stack.insert(0,ref[i])
            frames[j] = ref[i]
        else:
            x = stack.pop(-1)
            stack.insert(0,ref[i])
            for k in range(len(frames)):
                if frames[k] == x:
                    frames[k] = ref[i]

        print(f"\t{frames}",end='')      
    
        count += 1
        j += 1
        if j == 3:
            j = 0
    else:
        for k in range(len(stack)):
            if ref[i] == stack[k]:
                stack.pop(k)
                stack.insert(0,ref[i])
        print(" \t\t",end='')

    print(f"\t{stack}")
print(f"\ntotal number of page faults = {count}")
