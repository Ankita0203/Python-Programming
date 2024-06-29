import tkinter
from time import strftime

def clock():
    time1=strftime("%H  : %M :  %S  %p")
    label.config(text=time1,font=("Arial",80),bg="black",fg="yellow")
    label.after(1000,clock)

root=tkinter.Tk()
label=tkinter.Label(root)
label.pack()
clock()
root.mainloop()



