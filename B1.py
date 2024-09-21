import re
x=input("Enter a string :\n")
m=re.search(r"blde college",x)
if m!=None:
    print(m)
else:
    print("blde college not found")
mobile=re.findall(r"\d{10,10}",x)
print(mobile)
y=re.sub(r"blde college","kle college",x)
print(y)