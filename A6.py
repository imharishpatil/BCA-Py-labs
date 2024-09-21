n=int(input("Enter n value"))
x=[]
for i in range(0,n):
    v=int(input(f"enter {i} element :"))
    x.append(v)
key=int(input("enter item to searched"))
pos=-1
for i in range(0,n):
    if x[i]==key:
        pos=i
        break
    i+=1
if pos==-1:
    print("the item is not in the list")
else:
    print(f"the {key} found at {pos} position")