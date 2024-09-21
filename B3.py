stklst=[]
def add():
    global stklst
    item=input("enter the item to be inserted : ")
    stklst.append(item)
    print("item is inserted to stock")
    print("items in stock list")
    print(stklst)
    print(f"no of items presnt in stock list ={len(stklst)}")
def disp():
    global stklst
    n=int(input("eneter nth no of items"))
    x=stklst[:n]
    print("the first n items")
    for i in x:
        print(x)
def count():
    global stklst
    item=input("enetr the item to be counted")
    c=stklst.count(item)
    print(f"{item}={c}")
def filter():
    global stklst
    item=input("eneter the item to be filtered")
    flst=[e for e in stklst if e==item]
    print("the filtered item list")
    print(flst)
def delete():
    global stklst
    item=input("enter the item to be deleted")
    if item in stklst:
        stklst.remove(item)
        print("item has been removed")
    else:
        print("the item is not found in list")
while True:
    print("stack operations")
    print("1->Add item")
    print("2->Display")
    print("3->count")
    print("4->Filter")
    print("5->Delete")
    print("6->Exit")
    ch=int(input("eneter your choice : "))
    if ch==1:
        add()
    elif ch==2:
        disp()
    elif ch==3:
        count()
    elif ch==4:
        filter()
    elif ch==5:
        delete()
    elif ch==6:
        break
    else:
        print("enter the valid choice...")
    