n = int(input("Enter number of processes : "))
#p = [{"id":0, "arr":0, "burst":0}]
arrival = []
burst = []
finish = []
tat = []
wt = []

print()
print("Kindly enter the arrival time in ascending order\n")
for i in range(n):
    val = int(input(f"Enter arrival time for P{i} : "))
    arrival.append(val)

print()
for i in range(n):
    val = int(input(f"Enter CPU burst time for P{i} : "))
    burst.append(val)

t=0
for i in range(n):
    t += burst[i]
    finish.append(t)

for i in range(n):
    t = finish[i] - arrival[i]
    tat.append(t)
    t = tat[i] - burst[i]
    wt.append(t)


#for i in range(n):
    
print('\n')
print("processes \tarrival time \tburst time \tfinish time \tTAT \twaiting time")
for i in range(n):
    print(f"P{i} \t\t{arrival[i]} \t\t{burst[i]} \t\t{finish[i]} \t\t{tat[i]} \t{wt[i]}")

avg_wt = sum(wt)
avg_wt = avg_wt/n
print(f"\nAverage waiting time = {avg_wt}")

5
0
2
5
8
12
18
5
3
7
4


3
0
0
0
24
3
3
