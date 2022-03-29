ref = []
m = int(input("Enter number of characters in ref. string : "))
for i in range(m):
    print(f"  ref[{i}] : ", end='')
    x = int(input())
    ref.append(x)

#ref = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

n = int(input("\nEnter number of free frames : "))
frames = [0]*n
j = 0
count = 0 
for i in range(len(ref)):
    print(f"{ref[i]}", end='')
    if ref[i] not in frames:
        #frames.pop(0)
        #frames.append(ref[i])
        frames[j] = ref[i]
        print(f"\tpage fault \t{frames}")
        
        count += 1
        j += 1
        if j == 3:
            j = 0
    else:
        print()

print(f"\ntotal number of page faults = {count}")

20
1
2
3
4
2
1
5
6
2
1
2
3
7
6
3
2
1
2
3
6
3
