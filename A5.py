n=int(input("enter the n value"))
i=2
flag=False
while i==n//2:
    r=n%i
    if r==0:
        flag=True
        break
    i+=1
if flag==True:
    print(f"{n} is not prime no")
else:
    print(f"{n} is prime no")