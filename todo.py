import tkinter as tk

root = tk.Tk()


taskentry = tk.Text(master=root, font=("Inter", 12))
taskcreate = tk.Button(master=root, font=("Inter", 12))


def Strikethrough(x):
    res = ""    
    for c in x:
        res = res + c + "\u0336"
    return res


def oncheck(x):
    x.config(text=Strikethrough(x.cget("text")))
    x.config(state=tk.DISABLED)


def Create():
    task = tk.Checkbutton(text=taskentry.get(1.0, "end-1c"), font=("Inter", 12, "italic"))
    task.config(command=lambda: oncheck(task))
    task.pack()
    

taskcreate.config(command=Create, text="Create")





taskentry.pack()
taskcreate.pack()


tk.mainloop()