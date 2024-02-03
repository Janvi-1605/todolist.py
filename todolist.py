import tkinter
from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("waring", "please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

ws = Tk()
ws.geometry('500x450+500+200')
ws.title("TO DO LIST")
ws.config(bg='#3F027B')
ws.resizable(width=TRUE, height=TRUE)

frame=Frame(ws)
frame.pack(pady=20)

lb=Listbox(
    frame,
    width=25,
    height=8,
    #bg=''
    font=('Times', 15),
    bd=5,
    fg='#000003',
    highlightthickness=0,
    selectbackground='#000003',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

tasks_list=[]

for item in tasks_list:
    lb.insert(END, item)

sb=Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    ws, font=('times', 24)
)

my_entry.pack(pady=20)

Button_frame = Frame(ws)
Button_frame.pack(pady=20)

addTasl_btn=Button(
    Button_frame,
    text='Add task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTasl_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn=Button(
    Button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

    
ws.mainloop()
   




