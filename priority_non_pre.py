n = int(input("Enter no. of processes : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()

data = []       # job queue
ready = []      # ready queue

for i in range(n):
    process = {'id':0, 'arrival':0, 'burst':0, 'priority':0, 'finish':0, 'tat':0, 'wt':0}
    data.append(process)

for i in range(n):
    print()
    data[i]['id'] = i
    print(f"P{data[i]['id']}")

    data[i]['arrival']  = int(input("    Arrival Time   : "))
    data[i]['burst']    = int(input("    CPU Burst Time : "))
    data[i]['priority'] = int(input("    Priority       : "))

    
data.sort(key=lambda x : x['arrival'])

temp = data[:]  # for record    (won't get popped when data.pop())
temp2 = []      # for caculating values
time = 0        # for time simulations

print('\n')
for i in range(50):
    if i%2 == 0:
        print("-", end='')
    else:
        print(' ', end='')
print('\n')

#------------------------------------------

# ALGORITHM STARTS HERE
while data:
    # insert into ready queue
    for i in range(len(data)):
        if data[i]['arrival'] <= time:
            if data[i] not in ready:    # to avoid repition in ready queue
                ready.append(data[i])

    # sort ready queue in terms of priority
    ready.sort(key=lambda x : x['priority'])

    print(f"time {time}  \tReady queue : ", end='')
    for i in range(len(ready)):
        print(f"P{ready[i]['id']}  ", end='')

    # get lowest priority process from ready queue and execute
    exe = ready.pop(0)
    time = time + exe['burst']  # 'burst' time is elapsed

    print(f"\nP{exe['id']} completed at time = {time}") 

    exe['finish'] = time
    temp2.append(exe)

    # remove completed process from job queue
    for i in range(len(data)):
        if exe['id'] == data[i]['id']:
            data.remove(data[i])
            break

    if not data:
        print("\nAll processes completed")

    print()

wt=[]
for i in range(len(temp2)):
    temp2[i]['tat'] = temp2[i]['finish']-temp2[i]['arrival']
    temp2[i]['wt'] = temp2[i]['tat']-temp2[i]['burst']
    wt.append(temp2[i]['wt'])



print("\n\t  In the order of completion, using Priority Scheduling (non pre-emptive) Algorithm :-")
print("+-----------------------------------------------------------------------------------------------------+")
print("|  Processes \tArrival time \tBurst time \tPriority \tFinish Time \tTAT \tWaiting Time  |")
print("+-----------------------------------------------------------------------------------------------------+")
for i in range(len(temp2)):
    print(f"|  P{temp2[i]['id']} \t\t{temp2[i]['arrival']} \t\t{temp2[i]['burst']} ", end='')
    print(f"\t\t{temp2[i]['priority']} \t\t{temp2[i]['finish']}", end='')
    print(f"\t\t{temp2[i]['tat']} \t{temp2[i]['wt']} \t\t\b\b|")
print("+-----------------------------------------------------------------------------------------------------+")

avg_wt = sum(wt) / n
print(f"\nAverage waiting time = {avg_wt}")



4
0
8
2
0
4
3
6
2
1
10
9
4
