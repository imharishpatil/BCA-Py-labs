import cmath as m
a=int(input("Enter value for a : "))
b=int(input("Enter value for b : "))
c=int(input("Enter value for c : "))
d=b*b-4*a*c
if d>0:
    root1=-b+m.sqrt(d)/2*a
    root2=-b-m.sqrt(d)/2*a
    print("roots are real")
    print(f"root={root1} root2={root2}")
elif d==0:
    root1=root2=-b/2*a
    print("roots are equal")
    print(f"root1 & root2 is ={root1}")
else:
    root1=-b/2*a+m.sqrt(d)/2*a
    root2=-b/2*a-m.sqrt(d)/2*a
    print("roots are imaginary")
    print(f"root1={root1} root2={root2}")