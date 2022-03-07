from numpy import NaN


n = int(input("Enter no. of processes : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()

data = []       # job queue
ready = []      # ready queue

for i in range(n):
    process = {'id':0, 'arrival':0, 'burst':0, 'finish':0, 'tat':0, 'wt':0}
    data.append(process)

for i in range(n):
    print()
    data[i]['id'] = i
    print(f"P{data[i]['id']}")

    data[i]['arrival']  = int(input("    Arrival Time   : "))
    data[i]['burst']    = int(input("    CPU Burst Time : "))

    
data.sort(key=lambda x : x['arrival'])

temp = data[:]  # for record    (won't get popped when data.pop())
temp2 = []      # for caculating values
time = 0        # for time simulations
exe = {'id':NaN}

burst_list = []
for i in range(len(data)):
    b = {'id':data[i]['id'], 'burst':data[i]['burst']}
    burst_list.append(b)

print('\n')
for i in range(50):
    if i%2 == 0:
        print("-", end='')
    else:
        print(' ', end='')
print('\n')

print(f"time t  \tPn to be executed for 1 sec   (remaining burst = b)\n")

#------------------------------------------------------------

while data:
    for i in range(len(data)):
        if data[i]['arrival'] <= time:
            if data[i] not in ready:
                ready.append(data[i])


    ready.sort(key=lambda x : x['burst'])
    exe_prev = exe
    exe = ready.pop(0)
    if (exe['id'] != exe_prev['id']) and time != 0:
        print('--------------------------------------------------')
       

    if exe['burst'] == 0:
        # process completed
        print(f"time {time}  \tP{exe['id']}               finished")
        exe['finish'] = time
        temp2.append(exe)
        # process needs to be removed from job queue (data[])
        for i in range(len(data)):
            if exe['id'] == data[i]['id']:
                data.remove(data[i])
                break

    else:
        # process isn't complete
        exe['burst'] -= 1
        print(f"time {time}  \tP{exe['id']} - - - - (remaining burst = {exe['burst']})")
        ready.append(exe)
        time += 1

for i in range(len(temp)):
    temp[i]['burst'] = burst_list[i]['burst']


wt=[]
for i in range(len(temp2)):
    temp[i]['tat'] = temp[i]['finish']-temp[i]['arrival']
    temp[i]['wt'] = temp[i]['tat']-temp[i]['burst']
    wt.append(temp[i]['wt'])


print("\n\n       In the order of completion, using Shortest Remaining Time First Algorithm :-")
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


4
0
8
0
6
2
3
5
2
