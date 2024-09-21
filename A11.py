def write():
    uno=input("enter UUCMS :")
    name=input("enter Name :")
    line=f"{uno},{name}\n"
    file=open("student.csv","a")
    file.write(line)
    file.close()
    print("data written...")
def read():
    file=open("student.csv","r")
    data=file.readlines()
    print("student data is as follows")
    for line in data:
        print(line)
while True:
    print("file operations")
    print("1->write")
    print("2->read")
    print("3->Exit")
    ch=int(input("enter you choise"))
    if ch==1:
        write()
    elif ch==2:
        read()
    elif ch==3:
        break
    else:
        print("enter valid choise")