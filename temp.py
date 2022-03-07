def show(a,b,c,d):
    print("\n-------------------------------------")
    print("a")
    for i in range(len(a)):
        print(f"    {a[i]}")

    print("\nb")
    for i in range(len(b)):
        print(f"    {b[i]}")

    print("\nc")
    for i in range(len(c)):
        print(f"    {c[i]}")

    print("\nd")
    for i in range(len(d)):
        print(f"    {d[i]}")
    

a = []
dict1 = {'x':10, 'y':20}
dict2 = {'x':30, 'y':40}
dict3 = {'x':50, 'y':60}
a.append(dict1)
a.append(dict2)
a.append(dict3)

print("a")
for i in range(len(a)):
    print(f"    {a[i]}")

b = a
c = a[:]
d = a.copy()

dict4 = a.pop(0)
dict4['y'] = 100
a.append(dict4)

show(a,b,c,d)

#--------------------------------

a.pop()
show(a,b,c,d)