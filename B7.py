#exception
try:
    x=int(input("enter the first no = "))
    y=int(input("eneter the second no = "))
    z=x+y
    print(f"sum of 2 nums={z}")
except ValueError:
    print("value error")
finally:
    print("Thank you...")