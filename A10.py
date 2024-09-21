size=3
stack=[0]*3
top=-1
def push():
    global size,stack,top
    item=int(input("enter the item : "))
    if top==size-1:
        print("stack is full")
    else:
        top+=1
        stack[top]=item
        print(f"{item} pushed")
def pop():
    global stack,top
    if top==-1:
        print("stack is empty")
    else:
        top-=1
        print(f"item poped from the stack")
def display():
    global stack,top
    if top==-1:
        print("stack is empty")
    else:
        print("stack items as follows")
        for i in range(0,top+1):
            print(f"stack[{i}]={stack[i]}")
while True:
    print("***stack operations***")
    print("1->push")
    print("2->pop")
    print("3->display")
    print("4->Exit")
    ch=int(input("enter your choise"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        break
    else:
        print("enter valid choise")