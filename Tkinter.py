#GUI Tkinter
from tkinter import *
root=Tk()
label1=Label(root,text='Welcome to Python',background='red')
label2=Label(root,text='Have a Good Day',background='green')
label1.pack(fill=Y,padx=10,ipady=25,side=RIGHT)
label2.pack(fill=Y,padx=20,ipady=40,side=RIGHT)
root.mainloop()

from tkinter import *
root=Tk()
exitbutton=Button(root,text='Exit Program',command=root.destroy)
exitbutton.pack()
def my_callback():
    print("you clicked the message button")
msg_button=Button(root,text='Click Here',command=my_callback())
msg_button.pack()
root.mainloop()

from tkinter import *
root=Tk()
top_level_window=Toplevel()
top_level_window.title('Top Level Window')
def destroy_top_level_window():
    top_level_window.destroy() 
closebutton=Button(root,text='Close Top Level Window',command=destroy_top_level_window)
closebutton.pack()
root.mainloop()

from tkinter import *
root=Tk()
canvas=Canvas(root,width=250,height=200)
canvas.pack()
canvas.create_line(0,0,250,200,fill='orange',dash=(5,15))
canvas.create_rectangle(100,50,150,60,fill='red')
canvas.create_oval(30,30,50,50,fill='green')
root.mainloop()



