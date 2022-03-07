n = int(input("Enter no of processes : "))
if (n <= 0):
    print("Kindly enter a number greater than 0")
    exit()

data = []
q = []

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
#temp = data
# this doesn't work as the list isn't copied, 
# rather 'lvalue' becomes an alias

temp = data[:]      # for record
temp2 = []          # for calculation of values
time=0              # for time simulation

print('\n')
for i in range(50):
    if i%2 == 0:
        print("-", end='')
    else:
        print(' ', end='')
print('\n')

#print("\n-----------------------------------------------------------------------\n")

# ALGORITHM BEGINS HERE
while data: # continues till all processes are completed

    # insert into ready queue
    for i in range(len(data)):
        if (data[i]['arrival'] <= time):
            if (data[i] not in q):  # to avoid repetitive appending of processes in ready queue
                q.append(data[i])

    # after insertion into ready queue, sort queue in terms of burst time
    q.sort(key=lambda x: x['burst'])

    print(f"time {time}  \tReady queue : ", end='')
    for i in range(len(q)):
        print(f"P{q[i]['id']}  ", end='')
    
    exe = q.pop(0)
    time = time + exe['burst']

    print(f"\n{exe['id']} completed at time = {time}") 

    exe['finish'] = time
    temp2.append(exe)

    # remove the completed process from the list
    l = len(data)
    for i in range(len(data)):
        #print(f"{exe['id']} - {data[i]['id']}")
        if (exe['id'] == data[i]['id']):
            data.remove(data[i])
            # since the process is found, finish time input and deleted
            # from working list, no need to check any longer
            break
   
    if not data:
        print('\nAll processes completed')    
    
    print()

# temp is sorted in terms of id
# temp2 is sorted in terms of finish time 
# coz its appended as the processes are finished in real-time
'''for i in range(len(temp)):
    print(temp[i])

print()
for i in range(len(temp2)):
    print(temp2[i])
'''

wt=[]
for i in range(len(temp2)):
    temp2[i]['tat'] = temp2[i]['finish']-temp2[i]['arrival']
    temp2[i]['wt'] = temp2[i]['tat']-temp2[i]['burst']
    wt.append(temp2[i]['wt'])



print("\n\n\t    In the order of completion, using Shortest Job First Algorithm :-")
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
2
6
4
10
5
2
