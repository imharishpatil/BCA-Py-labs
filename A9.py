#selection sort
n=int(input("Enter n value :"))
x=[]
for i in range(0,n):
    v=int(input(f"enter {i} value : "))
    x.append(v)
for i in range(0,n):
    pos=i
    min=x[i]
    for j in range(i+1,n):
        if x[j]<min:
            pos=j
            min=x[j]
    temp=x[i]
    x[i]=x[pos]
    x[pos]=temp
print("sorted elements are")
for e in x:
    print(e)