import re
dob=input("enter your date of birth")
if re.match(r"^\d{2,2}\-\d{2,2}\-\d{4,4}$",dob):
    print("valid date of birth")
else:
    print("invalid d.o.b")