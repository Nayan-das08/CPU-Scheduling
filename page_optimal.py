'''ref = []
m = int(input("Enter number of characters in ref. string : "))
for i in range(m):
    print(f"  ref[{i}] : ", end='')
    x = int(input())
    ref.append(x)
'''

ref = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]

#print("ref.string \tframes \t\tstack")
#n = int(input("\nEnter number of free frames : "))
n = 3
frames = []
stack = []
p = 0
count = 0 
check = [0]*n
z = 0
for i in range(4):
    print(f" {ref[i]}\t", end='')
    
    if ref[i] not in frames:    # page fault

        if len(frames) < n:     # when frames[] isn't full
            frames.append(ref[i])
        else:                   # when frames[] is full
            for j in range(i+1, len(ref)):
                for k in range(n):
                    if ref[j] == frames[k]:
                        check[k] = 1
                        z += 1

                    
        print(f"\t{frames}", end='')
        print(f"\t{check}")
    print()
        