n=int(input("enter the n value"))
fib1=0
fib2=1
if n==fib1 or n==fib2:
    print(f"{n} belongs to the fib sequence")
else:
    flag=False
    fib3=0
    while fib3<n:
        fib3=fib1+fib2
        if fib3==n:
            flag=True
            break
        fib1=fib2
        fib2=fib3
if flag==True:
    print(f"{n} belongs to the fibonnaci sequence")
else:
    print(f"{n} not belongs to the fib sequence")