#tkinter
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry('600x500')
lbluno=tk.Label(form,text='UUCMS')
lbluno.grid(row=0,column=0,sticky=tk.W)
etuno=tk.Entry(form,width=20)
etuno.grid(row=0,column=1,padx=10,pady=5)
lblname=tk.Label(form,text='Name')
lblname.grid(row=1,column=0,sticky=tk.W)
etname=tk.Entry(form,width=20)
etname.grid(row=1,column=1,padx=10,pady=5)
gendervar=tk.StringVar()
gendervar.set(None)
lblgen=tk.Label(form,text='Gender')
lblgen.grid(row=2,column=0,sticky=tk.W)
rdbmale=tk.Radiobutton(form,variable=gendervar,value='male',text='Male')
rdbfemale=tk.Radiobutton(form,variable=gendervar,value='female',text='Female')
rdbmale.grid(row=2,column=1,padx=10,pady=5)
rdbfemale.grid(row=2,column=2,padx=10,pady=5)
lblnotify=tk.Label(form,text="get notification through")
lblnotify.grid(row=3,column=0,sticky=tk.W)
wappvar=tk.BooleanVar()
ckbwapp=tk.Checkbutton(form,variable=wappvar,text='Whatsapp')
ckbwapp.grid(row=3,column=1,padx=10,pady=5)
emailvar=tk.BooleanVar()
ckbemail=tk.Checkbutton(form,variable=emailvar,text='Email')
ckbemail.grid(row=3,column=2,padx=10,pady=5)
def save():
    uno=etuno.get()
    name=etname.get()
    gen=gendervar.get()
    wapp=wappvar.get()
    email=emailvar.get()
    row=f"UUCMS={uno} Name={name} Gender={gen}"
    if wapp:
        row=row+"get notification through whtsapp"
        if email:
            row=row+"and email"
    file=open('student1.csv','a')
    file.write(row)
    file.close()
    msgbox.showinfo("Message","Data saved...")
btnsave=tk.Button(form,text='save',command=save)
btnsave.grid(row=4,column=2,sticky=tk.W)
form.mainloop()