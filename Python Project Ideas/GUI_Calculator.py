import tkinter
from tkinter import *
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error" 
                messagebox.showerror("Error","Can not valid operation.")

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("350x550+500+75")
root.resizable(0,0) # ----------------------------> ReSizeble the Calcuator
root.title("Calculator By Dhruvin")
root.wm_iconbitmap('F:\Calc_logo.png')
root.iconphoto(False,tkinter.PhotoImage(file='F:\Calc_logo.png'))

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 45", justify=RIGHT)
screen.pack(fill = X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey" )
b = Button(f, text="C", padx=11, pady=8, font="lucida 30 bold",fg="orangered")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="()", padx=11, pady=8, font="lucida 30 bold", fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=11, pady=8, font="lucida 30 bold", fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=20, pady=8, font="lucida 30 bold", fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

# -------------------------------------------------------------------------------------


f = Frame(root, bg="grey" )
b = Button(f, text="7", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="8", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=17, pady=8, font="lucida 30 bold",fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

# ------------------------------------------------------------------------------------------------

f = Frame(root, bg="grey" )
b = Button(f, text="4", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="5", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=18, pady=8, font="lucida 30 bold", fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

# ------------------------------------------------------------------------------

f = Frame(root, bg="grey" )
b = Button(f, text="1", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="2", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=15, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=13, pady=8, font="lucida 30 bold", fg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

# -----------------------------------------------------------------------------------

f = Frame(root, bg="grey" )
b = Button(f, text="00", padx=4, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)


b = Button(f, text="0", padx=16, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=19, pady=8, font="lucida 30")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=16, pady=8, font="lucida 30 bold",fg="white", bg="orangered") # fg="orangered", bg="dodgerblue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()

mainloop()