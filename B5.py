#sqlite3
import sqlite3 as sql
con=sql.connect("ex.db")
cur=con.cursor()
sql="""
create table if not exists student
(
rno varchar(12),
name varchar(20),
primary key(rno)
)"""
cur.execute(sql)
cur.execute("delete from student")
for i in range(1,3):
    rno=input(f"enter the student {i} reg no : ")
    name=input(f"enetr the student {i} name : ")
    cur.execute("insert into student(rno,name) values(?,?)",(rno,name))
    con.commit()
    print("data inserted..")
def display():
    global cur
    cur.execute("select * from student")
    rows=cur.fetchall()
    print("student data is as follows")
    print("Reg No|\tName\t|")
    for row in rows:
        rno=row[0]
        name=row[1]
        print(f"{rno}|\t{name}\t|")
display()
rno=input("enter the reg no want to update : ")
name=input("enetr the correct name : ")
cur.execute("update student set name=? where rno=?",(name,rno))
con.commit()
print("data updated..")
display()
rno=input("enter the reg no want to delete : ")
cur.execute("delete from student where rno=?",(rno,))
con.commit()
print("data deleted")
display()
con.close()