n = int(input("Enter no of processes   : "))
q = int(input("Enter time quantum size : "))
if (n <= 0 or q <= 0):
    print("Kindly enter a number greater than 0")
    exit()

data = []   # job queue
ready = []  # ready queue

for i in range(n):
    process = {'id':0, 'arrival':0, 'burst':0, 'finish':0, 'tat':0, 'wt':0}
    data.append(process)

for i in range(n):
    print()
    data[i]['id'] = i
    print(f"P{data[i]['id']}")

    data[i]['arrival']  = int(input("    Arrival Time   : "))
    data[i]['burst']    = int(input("    CPU Burst Time : "))


data.sort(key=lambda x: x['arrival'])

burst_list = []
for i in range(len(data)):
    b = {'id':data[i]['id'], 'burst':data[i]['burst']}
    burst_list.append(b)

temp = data[:]  # for record (useless as any changes made to elements is reflected on it)
temp2 = []      # for calculation of values
time = 0

print('\n')
for i in range(50):
    if i%2 == 0:
        print("-", end='')
    else:
        print(' ', end='')
print('\n')

#print()
# ALGORITHM STARTS HERE
while data:
    # insert in ready queue
    for i in range(len(data)):
        if data[i]['arrival'] <= time:
            if data[i] not in ready:
                ready.append(data[i])

    exe = ready.pop(0)
    #print(exe)

    if exe['burst'] >= q:
        exe['burst'] = exe['burst'] - q
        # process not over even after one time quantum
        # process needs to be appended to ready queue
        print(f"time {time}  \tP{exe['id']} to be executed for {q} sec   (remaining burst = {exe['burst']})")
        ready.append(exe)
        time = time + q     # 'q' time has elapsed
    else:
        # process is comleted
        print(f"time {time}  \tP{exe['id']}         finished")#to be executed for {exe['burst']} sec       (finished)")
        time += exe['burst']    # 'burst' time has elapsed
        exe['burst'] = 0        # since process is over
        exe['finish'] = time    # at this 'time', process was finished
        temp2.append(exe)

        # process needs to be removed from job queue (data[])
        for i in range(len(data)):
            if exe['id'] == data[i]['id']:
                data.remove(data[i])
                break

# any change in temp is reflected in temp2
for i in range(len(temp)):
    temp[i]['burst'] = burst_list[i]['burst']

wt=[]
for i in range(len(temp2)):
    temp2[i]['tat'] = temp2[i]['finish']-temp2[i]['arrival']
    temp2[i]['wt'] = temp2[i]['tat']-temp2[i]['burst']
    wt.append(temp2[i]['wt'])

print("\n\n\t     In the order of completion, using Round Robin Algorithm :-")
print("+-------------------------------------------------------------------------------------+")
print("|  Processes \tArrival time \tBurst time \tFinish Time \tTAT \tWaiting Time  |")
print("+-------------------------------------------------------------------------------------+")
for i in range(n):
    print(f"|  P{temp2[i]['id']} \t\t{temp2[i]['arrival']}", end='')
    print(f"\t\t{temp2[i]['burst']} \t\t{temp2[i]['finish']}", end='')
    print(f"\t\t{temp2[i]['tat']} \t{temp2[i]['wt']} \t\t\b\b|")
print("+-------------------------------------------------------------------------------------+")

avg_wt = sum(wt) / n
print(f"\nAverage waiting time = {avg_wt}")

'''print()
for i in range(len(temp2)):
    print(temp2[i])
'''



4
4
0
10
1
6
3
2
5
4


4
4
0
12
0
6
3
2
5
4

3
4
0
24
0
3
0
5
