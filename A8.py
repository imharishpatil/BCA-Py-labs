#string functions
s=input("enter 5 names seprated by commas")
s1=s.upper()
print("converting all names to uppercase")
print(s1)
nlst=s.split(',')
print("the name list")
print(nlst)
print("removing extra spaces and capitalising first letter")
for n in nlst:
    n=n.strip()
    n=n.replace('  ',' ')
    n=n.capitalize()
    print(n)