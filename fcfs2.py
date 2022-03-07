# EXECUTE THIS ON WINDOWS TERMINAL / CMD.EXE
# IN CMD, \b DELETES ONE SPACE, NOT \t
# IN BASH, \b DELETES \t

n = int(input("Enter number of processes : "))
data = []

for i in range(n):
    process = {"id":0, "arrival":0, "burst":0, "finish":0, "tat":0, "wt":0}
    data.append(process)

# Getting values for arrival time and burst time from user
print()
for i in range(n):
    print()
    data[i]['id'] = i
    print(f"P{data[i]['id']}")

    data[i]['arrival']  = int(input("    Arrival Time   : "))
    data[i]['burst']    = int(input("    CPU Burst Time : "))

data.sort(key=lambda x: x['arrival'])

# Calculation
t = 0
wt = []
for i in range(n):
    t += data[i]['burst']
    data[i]['finish'] = t
    data[i]['tat'] = data[i]['finish'] - data[i]['arrival']
    data[i]['wt']  = data[i]['tat']    - data[i]['burst']
    wt.append(data[i]['wt'])



print("\n\n             In order of completion, using First-Come First-Serve Algorithm :-")
print("+-------------------------------------------------------------------------------------+")
print("|  Processes \tArrival time \tBurst time \tFinish Time \tTAT \tWaiting Time  |")
print("+-------------------------------------------------------------------------------------+")
for i in range(n):
    print(f"|  P{data[i]['id']} \t\t{data[i]['arrival']}", end='')
    print(f"\t\t{data[i]['burst']} \t\t{data[i]['finish']}", end='')
    print(f"\t\t{data[i]['tat']} \t{data[i]['wt']} \t\t\b\b|")
print("+-------------------------------------------------------------------------------------+")

avg_wt = sum(wt) / n
print(f"\nAverage waiting time = {avg_wt}")

# values as seen in table (in cmd)
5

8
12
5
0
2

7
4
3
18
5

# test values (copy these values)
5
8
7
12
4
5
3
0
18
2
5
